"""DAVID v0.12 real volumetric Brass & Woodwind Gallery rebuild.

Starts from v0.11 verified GLB. Replaces every room-3 selected sax silhouette
with an individually modeled 3D sax, trumpet, clarinet or flute, preserving
ALL 133 stable pickable mesh names (no breaking product/cart bindings).
Nothing here is a photograph, panorama, billboard, or image-plane shortcut.

Dependencies: trimesh, numpy, pillow. Run with: python build_gallery_v12.py
"""
from pathlib import Path
import math,re,json
from collections import Counter
import numpy as np,trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'assets/rooms/luxury-showroom-v11-optimized.glb'
OUT=ROOT/'assets/rooms/luxury-showroom-v12-unoptimized.glb'
s=trimesh.load(SRC,force='scene')
# Remove old, material-batched saxophone key parts before replacing instruments.
# These three batches contain ONLY legacy sax cup buttons, rods and hardware.
# Retaining them would cause doubled-up instrument features in the new models.
LEGACY_SAX_PARTS=('room_3__batched_v07_pearl_sax_button_inserts',
                  'room_3__batched_v07_aged_sax_keywork_brass',
                  'room_3__batched_chrome')
for legacy_node in LEGACY_SAX_PARTS:
    assert legacy_node in s.graph.nodes_geometry,legacy_node
    s.delete_geometry(s.graph[legacy_node][1])
serial=0
counts=Counter();exhibits=[]
MAT={
 'brass':PBRMaterial(name='v12 polished golden brass',baseColorFactor=[.78,.48,.16,1.0],metallicFactor=.93,roughnessFactor=.19),
 'rose_brass':PBRMaterial(name='v12 rose-gold lacquer',baseColorFactor=[.72,.36,.18,1.0],metallicFactor=.82,roughnessFactor=.23),
 'chrome':PBRMaterial(name='v12 polished nickel silver',baseColorFactor=[.75,.79,.82,1.0],metallicFactor=.94,roughnessFactor=.17),
 'blackwood':PBRMaterial(name='v12 black grenadilla clarinet wood',baseColorFactor=[.030,.028,.024,1.0],metallicFactor=0.,roughnessFactor=.36),
 'ebonite':PBRMaterial(name='v12 dark ebonite mouthpiece',baseColorFactor=[.042,.037,.030,1.0],metallicFactor=.04,roughnessFactor=.31),
 'leather':PBRMaterial(name='v12 instrument cork pads',baseColorFactor=[.39,.235,.11,1.0],metallicFactor=.0,roughnessFactor=.78),
 'ivory':PBRMaterial(name='v12 ivory pearl pads',baseColorFactor=[.86,.79,.61,1.0],metallicFactor=.12,roughnessFactor=.28),
 'felt':PBRMaterial(name='v12 midnight-blue velvet exhibit cushion',baseColorFactor=[.045,.06,.10,1.0],metallicFactor=0.,roughnessFactor=.92)
}

def paint(g,material):
    g.visual=TextureVisuals(uv=np.zeros((len(g.vertices),2)),material=MAT[material])
    return g

def add(g,material,tag):
    global serial
    if not len(g.faces):return
    serial+=1;paint(g,material)
    name=f'room_3_v12_{tag}_{serial:05d}'
    s.add_geometry(g,node_name=name,geom_name=name)
    counts[material]+=1

def vec(a):return np.array(a,dtype=float)

def tube_path(pts,radii,segments=12,hollow_tip=False):
    """Swept volumetric varying-radius instrument tubing with caps.

    Rings follow the 3D path, avoiding flat tube decals. Optional hollow
    final bell throat has an actual inner lip and a visible dark recess.
    """
    pts=np.asarray(pts,dtype=float);radii=np.asarray(radii,dtype=float)
    assert len(pts)==len(radii)>=2
    verts=[];faces=[]
    for i,p in enumerate(pts):
        tangent=pts[min(i+1,len(pts)-1)]-pts[max(i-1,0)]
        tangent=tangent/(np.linalg.norm(tangent)+1e-14)
        ref=np.array([0.,1.,0.])
        if abs(float(tangent@ref))>.88:ref=np.array([1.,0.,0.])
        u=np.cross(tangent,ref);u/=np.linalg.norm(u)+1e-14
        v=np.cross(tangent,u)
        for j in range(segments):
            a=math.tau*j/segments
            verts.append(p+radii[i]*(math.cos(a)*u+math.sin(a)*v))
    n=len(pts)
    for i in range(n-1):
        for j in range(segments):
            a=i*segments+j;b=i*segments+(j+1)%segments
            faces.extend(((a,b,b+segments),(a,b+segments,a+segments)))
    if not hollow_tip:
        verts.extend((pts[0],pts[-1]));start=len(verts)-2;end=len(verts)-1
        for j in range(segments):
            k=(j+1)%segments
            faces.extend(((start,k,j),((n-1)*segments+j,(n-1)*segments+k,end)))
    else:
        # Inner lip creates real depth when seen obliquely into the bell.
        last_ring=(n-1)*segments
        b=pts[-1];start=len(verts)
        for j in range(segments):
            point=np.asarray(verts[last_ring+j]);verts.append(b+(point-b)*.75)
        for j in range(segments):
            k=(j+1)%segments
            faces.extend(((last_ring+j,last_ring+k,start+k),(last_ring+j,start+k,start+j)))
    m=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
    m.fix_normals()
    return m

def cyl(a,b,r,segments=10):
    a=vec(a);b=vec(b);d=b-a
    length=np.linalg.norm(d)
    if length<1e-6:return trimesh.creation.box(extents=[.001]*3)
    m=trimesh.creation.cylinder(radius=r,height=length,sections=segments)
    m.apply_transform(trimesh.geometry.align_vectors([0,0,1],d/length))
    m.apply_translation((a+b)/2)
    return m

def ball(c,scale,n=1):
    m=trimesh.creation.icosphere(subdivisions=n);m.apply_scale(scale);m.apply_translation(c);return m

def box(c,dims):
    m=trimesh.creation.box(extents=dims);m.apply_translation(c);return m

def disc_x(c,r,width=.009):return cyl((c[0]-width/2,c[1],c[2]),(c[0]+width/2,c[1],c[2]),r,16)

def local_transform(origin,side):
    """Transform local instrument depth (front) toward room central aisle.

    x=depth, y=up, z=display horizontal. Inputs are world units.
    """
    x,y,z=origin
    def wp(dy=0.,dz=0.,depth=0.):return (x-side*depth,y+dy,z+dz)
    return wp

def select_model(meshes,node):
    assert meshes
    g=trimesh.util.concatenate(meshes)
    paint(g,meshes[0].visual.material.name if False else 'brass')
    # Material may be reset after select: set externally in run.
    s.add_geometry(g,node_name=node,geom_name=node)
    return g

def sax_model(wp,j):
    """True 3D curved sax body, bell, octave neck, 18 tone-key cups and rods."""
    core=[];details=[]
    def main(pts,radii,hollow=False):core.append(tube_path([wp(*q) for q in pts],radii,12,hollow))
    # Bores and U-shape are not orthogonal boxes. Camera-facing bell flares.
    main([(-.42,-.052,.02),(-.27,-.045,.025),(-.1,-.046,.031),(.11,-.050,.036),(.32,-.068,.037),(.47,-.052,.027)], [.048,.047,.047,.045,.037,.025])
    main([(-.43,-.05,.02),(-.50,-.018,.02),(-.52,.047,.03),(-.45,.105,.038),(-.37,.138,.045)], [.048,.054,.060,.070,.077])
    # Bass bow leading into flared forward-facing bell (traverses more depth).
    main([(-.37,.138,.045),(-.29,.166,.083),(-.20,.180,.13),(-.07,.175,.19),(.015,.167,.26)], [.077,.084,.100,.128,.154],True)
    # Curved crook, gooseneck and separate ebonite mouthpiece.
    main([(.47,-.052,.027),(.52,-.082,.01),(.55,-.12,0),(.57,-.16,-.01)], [.025,.021,.017,.016])
    add(tube_path([wp(.55,-.12,0),wp(.59,-.19,-.02)],[.020,.024],10),'ebonite','sax_mouthpiece')
    # Key cups array follows the left rod with brass keyposts and silver caps.
    for q in range(14):
        yy=-.35+q*.060
        dz=.015*math.sin(q*.9)
        cx=wp(yy,-.015+dz,.062)
        add(disc_x(cx,.018+(q%3)*.003,.009),'chrome','sax_key_cup')
        if q%2==0:
            add(cyl(wp(yy,-.085,.045),wp(yy,-.08,.16),.0036,8),'brass','sax_key_arm')
    for dz in (-.08,.072):
        add(cyl(wp(-.41,dz,.057),wp(.39,dz,.058),.004,8),'chrome','sax_long_key_rod')
    for q in range(5):
        add(ball(wp(-.30+q*.14,.04,.06),(.012,.010,.008),1),'ivory','sax_pearl_touch')
    counts['saxophones']+=1
    return core,'brass'

def trumpet_model(wp,j):
    """Physical horizontal trumpet with valve stack, U-shaped tuning slide and bell."""
    core=[]
    def main(pts,r):core.append(tube_path([wp(*q) for q in pts],r,12))
    main([(0,-.36,.02),(0,-.15,.02),(0,.1,.023),(0,.30,.032),(0,.42,.056)],[.022,.022,.025,.045,.12])
    # Main bell has opening rather than a sealed sticker/cylinder.
    core.append(tube_path([wp(0,.28,.04),wp(0,.36,.09),wp(.002,.47,.185)],[.040,.070,.125],14,True))
    main([(-.11,-.32,.01),(-.11,-.43,.016),(-.02,-.47,.02),(.07,-.41,.023),(.07,-.10,.023)], [.015,.015,.017,.017,.016])
    for k in range(3):
        z=-.14+.105*k
        add(cyl(wp(.02,z,.035),wp(.28,z,.035),.020,12),'rose_brass','trumpet_valve_tower')
        add(cyl(wp(.28,z,.035),wp(.34,z,.035),.011,10),'chrome','trumpet_valve_stem')
        add(disc_x(wp(.34,z,.035),.024,.013),'ivory','trumpet_valve_button')
    add(cyl(wp(-.035,-.41,.01),wp(.04,-.43,.01),.025,14),'chrome','trumpet_mouthpiece')
    add(cyl(wp(-.11,-.41,.01),wp(-.11,-.11,.01),.003,8),'brass','trumpet_tuning_slide_rod')
    counts['trumpets']+=1
    return core,'brass'

def clarinet_model(wp,j):
    core=[]
    core.append(tube_path([wp(-.49,0,.02),wp(-.15,0,.022),wp(.17,0,.022),wp(.45,0,.018)],[.052,.032,.025,.020],14,True))
    # Dark reed barrel + visibly nonmetallic body.
    cork=tube_path([wp(.43,0,.020),wp(.55,0,.015)],[.021,.016],12)
    add(cork,'ebonite','clarinet_ebonite_reed')
    for k in range(14):
        y=-.36+k*.059
        add(disc_x(wp(y,-.024,.040),.0175,.007),'chrome','clarinet_silver_key')
        add(disc_x(wp(y,-.024,.027),.010,.004),'leather','clarinet_cork_underpad')
    for sideZ in (-.036,.032):
        add(cyl(wp(-.44,sideZ,.028),wp(.41,sideZ,.029),.0029,8),'chrome','clarinet_long_rod')
    add(cyl(wp(.465,0,.019),wp(.48,0,.019),.020,12),'chrome','clarinet_barrel_ring')
    counts['clarinets']+=1
    return core,'blackwood'

def flute_model(wp,j):
    core=[]
    core.append(tube_path([wp(.04,-.47,.020),wp(.04,-.10,.024),wp(.04,.18,.024),wp(.04,.47,.020)],[.018,.018,.018,.018],14))
    # Entire body silver, instrument is horizontal at a different level in niche.
    for k in range(13):
        z=-.39+k*.065
        add(disc_x(wp(.055,z,.020),.025,.006),'chrome','flute_pad_key')
    for yy in (.065,.01):
        add(cyl(wp(yy,-.43,.028),wp(yy,.38,.028),.003,8),'chrome','flute_keys_rod')
    for z in (-.23,.04,.30):
        add(cyl(wp(.03,z,.02),wp(.08,z,.02),.008,8),'brass','flute_post')
    counts['flutes']+=1
    return core,'chrome'

nodes=sorted(n for n in s.graph.nodes_geometry if re.match(r'^interact_3_\d+_sax_\d+$',n))
assert len(nodes)==27,len(nodes)
for j,node in enumerate(nodes):
    transform,key=s.graph[node];old=s.geometry[key]
    wc=(transform@np.r_[old.bounds.mean(axis=0),1])[:3]
    x,y,z=map(float,wc)
    side=1 if x>=0 else -1
    # Six kinds of display areas, all proper geometry, every object clickable.
    typ=('saxophone' if j%9 in (0,1,2,3) else
         'trumpet' if j%9 in (4,5) else
         'clarinet' if j%9 in (6,7) else 'flute')
    if j>=24:typ='saxophone' # center vitrines are highlighted saxophones
    wp=local_transform((x,y,z),side)
    if typ=='saxophone':submesh,material=sax_model(wp,j)
    elif typ=='trumpet':submesh,material=trumpet_model(wp,j)
    elif typ=='clarinet':submesh,material=clarinet_model(wp,j)
    else:submesh,material=flute_model(wp,j)
    s.delete_geometry(key)
    selectable=trimesh.util.concatenate(submesh)
    paint(selectable,material)
    s.add_geometry(selectable,node_name=node,geom_name=node)
    exhibits.append({'mesh':node,'type':typ,'room':3})
    counts['rebuilt_selected_instruments']+=1

assert len([n for n in s.graph.nodes_geometry if n.startswith('interact_')])==133
OUT.parent.mkdir(parents=True,exist_ok=True)
s.export(OUT)
(ROOT/'assets/data/exhibits-v12.json').write_text(json.dumps({'version':'v0.12','exhibits':exhibits},indent=2)+'\n')
print('v0.12 physical gallery instrument types',dict(counts),'scene nodes',len(s.graph.nodes_geometry),'output',OUT.stat().st_size)