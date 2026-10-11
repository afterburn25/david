"""DAVID 0.6: distinct boutique spaces, real beveled guitars and bespoke interiors.

This intentionally extends the authored 0.5 world-space GLB. Approved photos are
reference-only and NEVER projected onto geometry. No external unlicensed asset.
Run: python build_gallery_v06.py && python optimize_gallery_v06.py
"""
from __future__ import annotations
from pathlib import Path
import re, math, numpy as np, trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals
from PIL import Image
from shapely.geometry import Polygon
from shapely.ops import triangulate
import build_gallery_v05 as v05

v04=v05.prior
b=v04.b
OUT=Path(__file__).resolve().parent/'assets/rooms/luxury-showroom-v06.glb'

# New tactile PBR materials complement the earlier model, without photography.
def pbr(key,name,color,rough=.55,metal=.0,emissive=None):
    kwargs={'name':name,'baseColorFactor':[*color,1], 'roughnessFactor':rough,'metallicFactor':metal}
    if emissive:kwargs['emissiveFactor']=emissive
    b.M[key]=PBRMaterial(**kwargs)
pbr('cognac06','Soft cognac leather upholstery',[.57,.26,.13],.79)
pbr('ivory_linen06','Warm ivory basketweave linen',[.68,.58,.46],.96)
pbr('navy_velvet06','Electric vault midnight velvet',[.09,.12,.17],.91)
pbr('showcase_walnut06','Dark fluted walnut marquetry',[.12,.065,.038],.53)
pbr('amber_plaster06','Warm amber niche illuminated plaster',[.43,.34,.24],.84,emissive=[.16,.08,.036])
pbr('limestone06','Subtle champagne stone',[.39,.32,.26],.69)
pbr('gold_leaf06','Hand-brushed antique gold',[.66,.42,.16],.28,.87)
pbr('key_marble06','Portoro black stone and gold',[.071,.061,.050],.22,.08)
pbr('oak06','Acoustic hall blonde oak',[.50,.32,.15],.66)
pbr('amplifier06','Black braided amplifier textile',[.10,.096,.083],.94)
pbr('electric_blue06','Electric vault cobalt lacquer',[.025,.06,.19],.18,.23)

# A modeled guitar needs volume with bevels, not a thick flat silhouette.
# Spline-smoothed sides continue behind the instrument; no camera-facing plane.
def catmull_closed(points,subdiv=6):
    p=np.asarray(points,float);res=[];count=len(p)
    for i in range(count):
        q0,q1,q2,q3=(p[(i+j)%count] for j in (-1,0,1,2))
        for t in np.linspace(0,1,subdiv,endpoint=False):
            vec=.5*((2*q1)+(-q0+q2)*t+(2*q0-5*q1+4*q2-q3)*t*t+(-q0+3*q1-3*q2+q3)*t*t*t)
            res.append(vec)
    return np.array(res)

def loft_body(profile,transform):
    path=catmull_closed(profile,7)
    center=path.mean(axis=0)
    N=len(path);layers=[(-.058,.956),(-.046,1),(.046,1),(.058,.956)]
    verts=[];faces=[]
    for thick,shrink in layers:
        for xx,yy in path:
            v=center+(np.array([xx,yy])-center)*shrink
            verts.append((v[0],v[1],thick))
    for ring in range(len(layers)-1):
        for j in range(N):
            a=ring*N+j;nextj=ring*N+(j+1)%N
            faces.extend([(a,nextj,nextj+N),(a,nextj+N,a+N)])
    # The bevelled top and bottom are geometrically filled, not just outline loops.
    for layer,front in ((0,False),(3,True)):
        base=layer*N
        coord_to_idx={tuple(np.round(v[:2],5)):base+i for i,v in enumerate(verts[base:base+N])}
        ring_xy=[v[:2] for v in verts[base:base+N]]
        poly=Polygon(ring_xy)
        for tri in triangulate(poly):
            if not poly.covers(tri.representative_point()):continue
            face=[]
            for xy in list(tri.exterior.coords)[:3]:
                key=tuple(np.round(xy,5))
                if key not in coord_to_idx:
                    coord_to_idx[key]=len(verts);verts.append((float(xy[0]),float(xy[1]),layers[layer][0]))
                face.append(coord_to_idx[key])
            faces.append(tuple(face if front else face[::-1]))
    mesh=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
    mesh.apply_transform(transform)
    mesh.fix_normals()
    return mesh

# Replace selected front guitar bodies in situ while keeping exactly the same
# canonical selection nodes and their product mappings: 322 picks remain stable.
upgraded=[]
for node in tuple(b.scene.graph.nodes_geometry):
    match=re.match(r'^interact_0_(\d+)_guitar_(\d+)$',node)
    if not match:continue
    slot=int(match.group(1))
    transform,key=b.scene.graph[node]
    old=b.scene.geometry[key]
    center=old.bounds.mean(axis=0)
    if slot>=100:
        T=b.tx_rot(3.08+(slot-100)*.96,1.98,.20,0)
    else:
        x=center[0]; side=-1 if x<0 else 1
        T=b.tx_rot(side*8.99,2.50,center[2],math.pi/2 if side<0 else -math.pi/2)
    new=loft_body(b.ELECTRIC,T)
    new.visual=TextureVisuals(uv=np.zeros((len(new.vertices),2)),material=old.visual.material)
    b.scene.delete_geometry(key)
    b.scene.add_geometry(new,node_name=node,geom_name=node)
    upgraded.append(node)
assert len(upgraded)==27,(len(upgraded),upgraded)

# The approved gallery photographs show TWO stacked tiers of guitars. Instead of
# copying photographs into upper bays, duplicate *actual volume meshes* and
# relocate complete original instruments; only the lower tier remains interactive
# so existing 322 product IDs never change. Every upper tier has a real back.
V03_GUITAR_PARTS=('guitar_neck_','guitar_fretboard_','guitar_headstock_',
 'fret_','string_','guitar_tuner_','guitar_pickup_','guitar_bridge_',
 'guitar_soundhole_','control_knob_')
tier_stats={}
for room in (0,1,2):
    target=[]
    zmin=room*23.5-11.0;zmax=room*23.5+11.0
    for node in tuple(b.scene.graph.nodes_geometry):
        tr,key=b.scene.graph[node]
        geom=b.scene.geometry[key]
        centre=geom.bounds.mean(axis=0)
        if not (abs(centre[0])>8.55 and zmin<centre[2]<zmax and 1.15<centre[1]<4.95):continue
        isbody=bool(re.match(rf'^interact_{room}_\d+_guitar_\d+$',node))
        other=(node.startswith(V03_GUITAR_PARTS) or
               (room==0 and node.startswith('room_0_v05_guitar_hardware')))
        if isbody or other:target.append((node,key,tr,geom.copy()))
    for node,key,tr,original in target:
        # Upper row (non-DB display) sits wholly inside its recessed bay.
        high=original.copy();high.apply_translation((0,1.04,0))
        b.scene.add_geometry(high,node_name=f'room_{room}_uppertier_{node}',geom_name=f'room_{room}_uppertier_{node}')
        # Original named lower tier retains its exact stable pick ID.
        low=original.copy();low.apply_translation((0,-1.13,0))
        b.scene.delete_geometry(key)
        b.scene.add_geometry(low,node_name=node,geom_name=node)
    tier_stats[room]=len(target)
    for side in (-1,1):
        for k in range(6):
            zz=room*23.5-9.3+k*3.55
            b.box(side*9.22,3.055,zz,.22,.095,3.12,'showcase_walnut06',f'room_{room}_v06_double_tier_divider')
            b.box(side*9.09,3.01,zz,.035,.028,3.02,'gold_leaf06',f'room_{room}_v06_double_tier_gold_trim')
assert all(tier_stats[room]>=24 for room in (0,1,2)),tier_stats
print('v0.6 double-tier actual 3D instruments:',tier_stats)

# Remove only generic lounge geometry in first two galleries; keep other rooms.
for node in tuple(b.scene.graph.nodes_geometry):
    if node.startswith(('room_0_premium_lounge','room_1_premium_lounge')):
        b.scene.delete_geometry(b.scene.graph[node][1])

# High-order sculpted cushions, separate inset upholstery and trim, no cube sofa.
def cushion(x,y,z,sx,sy,sz,mat,label,sub=3):
    m=trimesh.creation.icosphere(subdivisions=sub,radius=1)
    m.apply_scale((sx,sy,sz));m.apply_translation((x,y,z));b.put(m,mat,label)

def sofa(room,center_x,center_z,fabric):
    label=f'room_{room}_v06_bespoke_lounge'
    b.box(center_x,.22,center_z,3.95,.30,1.65,'showcase_walnut06',label+'_base_frame')
    for j,xoff in enumerate((-1.17,0,1.17)):
        cushion(center_x+xoff,.64,center_z-.23,.67,.26,.66,fabric,label+'_deep_feather_seat')
        cushion(center_x+xoff,1.03,center_z+.62,.66,.42,.24,fabric,label+'_lumbar_bolster')
        for px in (-.28,.28):
            b.pipe((center_x+xoff+px,.835,center_z+.79),(center_x+xoff+px,.905,center_z+.79),.007,'gold_leaf06',label+'_button_stitch',8)
        # Loose textile pillow with rounded actual 3-D corner silhouette.
        cushion(center_x+xoff+.31,.89,center_z+.46,.24,.29,.10,'ivory_linen06',label+'_pillow')
    for side in (-1,1):
        cushion(center_x+side*1.80,.75,center_z,.21,.42,.81,fabric,label+'_scrolling_armrest')
        for zz in (-.68,.62):
            b.pipe((center_x+side*1.72,.06,center_z+zz),(center_x+side*1.72,.25,center_z+zz),.033,'gold_leaf06',label+'_brass_feet',8)
    # Circular genuine stone tabletop on ribbed brass drum.
    v04.oval(center_x-.20,.38,center_z-2.02,1.12,.10,.68,'key_marble06',label+'_oval_portoro_table')
    v04.oval(center_x-.20,.24,center_z-2.02,.82,.19,.49,'gold_leaf06',label+'_oval_bronze_base')
    for j in range(48):
        a=j*2*math.pi/48
        x=center_x-.20+.80*math.cos(a);z=center_z-2.02+.47*math.sin(a)
        b.pipe((x,.11,z),(x,.41,z),.008,'showcase_walnut06',label+'_table_fluting',7)
    # Opposite luxuriously upholstered chair and matching low footrest.
    cushion(center_x-3.00,.58,center_z-2.11,.71,.28,.64,fabric,label+'_club_chair_seat')
    cushion(center_x-3.00,.99,center_z-1.77,.70,.47,.29,fabric,label+'_club_chair_back')
    for off in (-.64,.64):
        cushion(center_x-3.00+off,.65,center_z-2.00,.15,.36,.67,fabric,label+'_club_chair_armrest')

sofa(0,-3.15,-2.4,'cognac06')
sofa(1,-3.15,23.5-2.4,'ivory_linen06')

# Signature wall: full-height bronze-ribbed feature partition immediately beyond
# central circular vitrines. This is world-space architecture, not a photo poster.
for room in (0,1):
    z=room*23.5
    name=f'room_{room}_v06_feature'
    if room==0:
        b.box(4.10,3.02,z+3.38,3.78,5.68,.22,'showcase_walnut06',name+'_stone_portal_core')
        for j in range(43):
            xx=2.29+j*.086
            b.box(xx,3.08,z+3.23,.025,5.45,.032,'gold_leaf06' if j%8==0 else 'espresso',name+'_vertical_rib')
        for yy in (.33,5.76):
            b.box(4.1,yy,z+3.17,3.86,.024,.025,'warm_led',name+'_rim_backlight')
        for x in (2.12,6.07):b.box(x,3.0,z+3.14,.024,5.58,.03,'gold_leaf06',name+'_reveal')
    else:
        # Seated consultation nook: stools and elegant oak tasting table.
        v04.oval(-5.35,.82,z+4.65,1.12,.09,.68,'oak06',name+'_consultation_table')
        for i in range(3):
            angle=-.3+i*2.4
            x=-5.35+1.45*math.cos(angle);zz=z+4.65+.91*math.sin(angle)
            cushion(x,.56,zz,.39,.14,.40,'ivory_linen06',name+'_consultation_chair')
            b.pipe((x,.07,zz),(x,.48,zz),.028,'gold_leaf06',name+'_chair_leg')

# Stairway and actual upper landing only in the main gallery. The other four
# rooms get distinct signature furnishings instead of copied boutique corridors.
basez=0
label='room_0_v06_staircase'
for k in range(16):
    y=.125+(k+1)*.215;z=5.10+k*.345
    b.box(7.00,y/2,z,2.30,y,.32,'showcase_walnut06',label+'_closed_riser')
    b.box(7.00,y+.018,z,2.30,.042,.355,'limestone06',label+'_stone_tread')
    b.box(7.00,y+.044,z-.15,2.30,.018,.018,'gold_leaf06',label+'_tread_nosing')
for side in (-1,1):
    xx=7.00+side*1.20
    for k in range(0,16,2):
        y=.125+(k+1)*.215
        z=5.10+k*.345
        b.pipe((xx,y,z),(xx,y+1.0,z),.014,'gold_leaf06',label+'_baluster')
    b.pipe((xx,1.31,5.06),(xx,4.60,10.31),.028,'gold_leaf06',label+'_inclined_hand_rail')

# Electric Vault amp wall: drivers are actual conic/circular meshes and knobs.
for i in range(4):
    z=47-8.1+i*3.0
    label='room_2_v06_amplifier_wall'
    b.box(-7.90,.56,z,1.18,.90,.52,'amplifier06',label+'_speaker_cabinet')
    b.box(-7.90,1.06,z,1.18,.10,.52,'gold_leaf06',label+'_control_header')
    for offset in (-.31,.31):
        # Drivers face into the aisle (normal +x), not 2-D disk cutouts.
        m=trimesh.creation.cone(radius=.26,height=.035,sections=30)
        m.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[0,1,0]))
        m.apply_translation((-7.56,.57,z+offset))
        b.put(m,'black',label+'_woofer_cone')
        b.pipe((-7.52,.57,z+offset),(-7.49,.57,z+offset),.095,'gold_leaf06',label+'_woofer_dustcap',18)
    for knob in range(6):
        zknob=z-.42+knob*.165
        b.pipe((-7.50,1.09,zknob),(-7.44,1.09,zknob),.018,'steel',label+'_control_knob',10)

# Brass gallery museum cases and piano salon recital plinth with actual 3-D trim.
for room in (3,4):
    z=room*23.5
    label=f'room_{room}_v06_signature'
    if room==3:
        for side in (-1,1):
            x=side*5.90
            b.box(x,.40,z+5.52,2.1,.76,1.15,'showcase_walnut06',label+'_archive_plinth')
            b.box(x,.80,z+5.52,2.1,.025,1.15,'gold_leaf06',label+'_under_glass_trim')
            for xx in (-.98,.98):
                for zz in (-.49,.49):
                    b.pipe((x+xx,.85,z+5.52+zz),(x+xx,3.12,z+5.52+zz),.017,'gold_leaf06',label+'_glass_corner')
            b.box(x,3.10,z+5.52,2.02,.046,1.05,'gold_leaf06',label+'_lightbar')
    else:
        # Stone recital stage is centered around the existing playable piano.
        v04.oval(3.50,.045,z+.20,2.58,.055,2.07,'key_marble06',label+'_oval_recital_plinth')
        v04.trim_circle(3.50,.11,z+.20,2.6,2.08,.013,'gold_leaf06',label+'_plinth_gold_edge',72)
        for x in (2.0,5.0):
            b.pipe((x,5.4,z-2.7),(x,3.12,z-2.7),.015,'gold_leaf06',label+'_suspended_lamp')
            b.pipe((x,3.25,z-2.7),(x,3.00,z-2.7),.045,'warm_led',label+'_suspended_lamp_glow')

# Correct inherited v0.3 UV=0 for most non-floor geometry. Textures with a
# constant UV show only one flat texel: bad for leather, walnut and PBR normals.
# Apply authored metre-scale planar UVs to real triangles for each mesh plane;
# geometry remains 3D (this is *not* a projection of a showroom photograph).
from PIL import ImageFilter
for key in ('wood','rug','carpet','marble','leather','wall'):
    material=b.M[key]
    img=material.baseColorTexture
    if img is None:continue
    height=np.asarray(img.convert('L'),dtype=np.float32)/255
    dy,dx=np.gradient(height)
    strength={'wood':18,'rug':25,'carpet':21,'marble':7,'leather':17,'wall':6}[key]
    vx=-dx*strength;vy=-dy*strength;vz=np.ones_like(vx)
    norm=np.sqrt(vx*vx+vy*vy+vz*vz)
    rgb=np.stack((vx/norm,vy/norm,vz/norm),axis=2)*.5+.5
    material.normalTexture=Image.fromarray(np.uint8(np.clip(rgb*255,0,255)),'RGB')
uv_corrected=0
for geom in b.scene.geometry.values():
    material=getattr(geom.visual,'material',None)
    if material is None or getattr(material,'baseColorTexture',None) is None:continue
    uv=np.asarray(getattr(geom.visual,'uv',None))
    if uv.shape!=(len(geom.vertices),2) or not np.allclose(uv,0):continue
    verts=np.asarray(geom.vertices)
    spans=np.ptp(verts,axis=0)
    axes=np.argsort(spans)[-2:][::-1]
    scale=.68 if 'leather' in material.name.lower() else 1.24
    coords=verts[:,axes]/scale
    geom.visual.uv=np.asarray(coords,dtype=np.float64)
    uv_corrected+=1
print('v0.6 real-mesh PBR UV corrections:',uv_corrected,'procedural tangent normal maps: 6')

OUT.parent.mkdir(parents=True,exist_ok=True)
b.scene.export(OUT)
reimport=trimesh.load(OUT,force='scene')
picks=sorted(n for n in reimport.graph.nodes_geometry if n.startswith('interact_'))
assert len(picks)==322,len(picks)
print('v0.6 genuine modeled GLB',OUT.stat().st_size,'bytes',len(reimport.graph.nodes_geometry),'nodes',len(picks),'selectable')