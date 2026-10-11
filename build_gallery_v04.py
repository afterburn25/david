"""DAVID v0.4: architecture + premium display geometry refinement.

Builds on tracked deterministic v0.3 authored GLB geometry. Approved generated
photographs are used only as *visual references*, never flat image textures.
No proprietary furniture/instrument models or unlicensed assets used.
"""
from pathlib import Path
import math
import numpy as np
import trimesh
from PIL import Image, ImageFilter
from trimesh.visual.material import PBRMaterial

ROOT=Path(__file__).resolve().parent
source=ROOT/'build_gallery_v03.py'
# v0.3 generated seven separate *selectable* sax tube segments per instrument.
# Keep the first segment and bell selectable; batch the others with scenery.
# This does not reduce visual geometry, only unnecessary raycast/draw nodes.
base_source=source.read_text().replace(
    "for a,b in zip(pts,pts[1:]):localpipe(a,b,.031,'brass',f'interact_{room}_{slot}_sax',T,10)",
    "for n,(a,b) in enumerate(zip(pts,pts[1:])):localpipe(a,b,.031,'brass',f'interact_{room}_{slot}_sax' if n==0 else 'sax_body',T,10)"
)
assert base_source!=source.read_text(), 'Expected original sax source marker missing'
ns={'__file__':str(source),'__name__':'__main__'}
exec(compile(base_source,str(source),'exec'),ns)
scene=ns['scene'];M=ns['M']
box=ns['box'];plane=ns['plane'];pipe=ns['pipe'];orb=ns['orb'];put=ns['put']
localpipe=ns['localpipe'];localbox=ns['localbox'];tx_rot=ns['tx_rot']
extrude_profile=ns['extrude_profile'];guitar=ns['guitar']

# Remove v0.3 room-blocking primitive furnishings and square showcases. Model
# properly shaped replacement furnishings; keep all 3D instruments and backdrop.
remove_terms=('rounded_seat','sofa_seat','sofa_back','sofa_arm','sofa_pillow',
              'lounge_chair','chair_back','marble_coffee_table','coffee_table_legs',
              'island_base','island_vertical_rib','showcase_front_glass',
              'showcase_back_glass','showcase_side_glass','glass_case_frame')
remove=[k for k in scene.geometry if any(t in k for t in remove_terms)]
scene.delete_geometry(remove)

M.update({
 'leather_dark':PBRMaterial(name='Full grain dark chocolate leather',baseColorFactor=[.155,.081,.053,1],metallicFactor=0,roughnessFactor=.52),
 'leather_light':PBRMaterial(name='Warm cognac saddle leather',baseColorFactor=[.29,.13,.067,1],metallicFactor=0,roughnessFactor=.51),
 'linen':PBRMaterial(name='Textured taupe boucle',baseColorFactor=[.54,.47,.39,1],metallicFactor=0,roughnessFactor=.96),
 'velvet':PBRMaterial(name='Charcoal soft velvet',baseColorFactor=[.115,.106,.104,1],metallicFactor=0,roughnessFactor=.95),
 'dark_marble':PBRMaterial(name='Dark Nero Marquina stone',baseColorFactor=[.067,.064,.06,1],metallicFactor=.08,roughnessFactor=.18),
 'antique_gold':PBRMaterial(name='Antique brushed champagne brass',baseColorFactor=[.66,.43,.19,1],metallicFactor=.89,roughnessFactor=.27),
 'gold_metal':PBRMaterial(name='Gold lacquered brass',baseColorFactor=[.81,.60,.24,1],metallicFactor=.86,roughnessFactor=.20),
 'antique_copper':PBRMaterial(name='Aged copper alloy',baseColorFactor=[.49,.27,.14,1],metallicFactor=.75,roughnessFactor=.25),
 'warm_cream':PBRMaterial(name='Biscuit plaster',baseColorFactor=[.59,.47,.34,1],metallicFactor=0,roughnessFactor=.90),
 'vintage_white':PBRMaterial(name='Vintage Ivory',baseColorFactor=[.92,.83,.66,1],metallicFactor=.08,roughnessFactor=.31),
 'ebony':PBRMaterial(name='Deep black ebony',baseColorFactor=[.023,.023,.025,1],metallicFactor=.22,roughnessFactor=.23),
 'emissive_amber':PBRMaterial(name='Warm hidden LED 2900K',baseColorFactor=[1,.66,.31,1],emissiveFactor=[1,.42,.11],metallicFactor=.06,roughnessFactor=.38),
 'cream_wall':PBRMaterial(name='Warm travertine wall',baseColorFactor=[.55,.44,.34,1],metallicFactor=0,roughnessFactor=.87),
 'olive':PBRMaterial(name='Olive silk leaves',baseColorFactor=[.10,.17,.065,1],roughnessFactor=.85),
})

def custom_tex(mode,N=512):
    yy,xx=np.indices((N,N));r=np.random.default_rng(1105+len(mode))
    noise=r.normal(0,1,(N,N))
    if mode=='Persian wool botanical carpet':
        u=(xx-N/2)/(N/2);v=(yy-N/2)/(N/2)
        wavy=(np.sin(xx*.074+np.sin(yy*.017)*2)+np.sin(yy*.103+np.cos(xx*.025)))*5
        border=((abs(u)>.83)|(abs(v)>.83)).astype(float)
        border2=((abs(u)>.74)|(abs(v)>.74)).astype(float)
        med=np.exp(-((u/.54)**4+(v/.57)**4)*1.9)
        a=np.stack([127+med*24-border*35-border2*7+wavy+noise*9,
                    118+med*17-border*27-border2*7+wavy*.7+noise*9,
                    105+med*10-border*23-border2*7+wavy*.65+noise*9],-1)
    elif mode=='Walnut vertical slat':
        grain=13*np.sin(xx*.23+3*np.cos(yy*.006))+6*np.sin(xx*1.23)
        slat=np.maximum(0,np.sin(xx*.22))**13
        a=np.stack([84+grain-slat*38+noise*2,49+grain*.56-slat*26+noise*2,26+grain*.31-slat*19+noise*2],-1)
    elif mode=='Leather grain':
        dots=np.sin(xx*.86)*np.sin(yy*.95)*3
        a=np.stack([110+noise*6+dots,58+noise*4+dots*.5,36+noise*4+dots*.3],-1)
    elif mode=='Polished black marble veins':
        fx=xx*.026+yy*.011+3.8*np.sin(yy*.012+np.sin(xx*.012))
        veins=(np.abs(np.sin(fx))>.983).astype(float)*38
        a=np.stack([31+veins+noise*3,29+veins*.93+noise*3,29+veins*.85+noise*3],-1)
    else:raise KeyError(mode)
    return Image.fromarray(np.uint8(np.clip(a,0,255)),'RGB').filter(ImageFilter.GaussianBlur(.3))
def bump_normals(im, strength):
    lum=np.asarray(im.convert('L').filter(ImageFilter.GaussianBlur(1.1)),dtype=np.float32)/255.0
    dy,dx=np.gradient(lum);a=-dx*strength;b=-dy*strength
    n=np.stack([a,b,np.ones_like(a)],-1);n/=np.linalg.norm(n,axis=-1,keepdims=True)
    return Image.fromarray(np.uint8(np.clip((n*.5+.5)*255,0,255)),'RGB')
for key,metal,rough in [('wool_detail',0,.98),('walnut_slat',.03,.55),('grain_leather',0,.62),('stone_detail',.08,.21)]:
    mapping={'wool_detail':'Persian wool botanical carpet','walnut_slat':'Walnut vertical slat','grain_leather':'Leather grain','stone_detail':'Polished black marble veins'}
    M[key]=PBRMaterial(name=mapping[key],baseColorTexture=custom_tex(mapping[key]),
        normalTexture=bump_normals(custom_tex(mapping[key]),{"wool_detail":5.0,"walnut_slat":3.4,"grain_leather":2.4,"stone_detail":2.0}[key]),
        baseColorFactor=[.86,.86,.86,1],metallicFactor=metal,roughnessFactor=rough)

def ellipsoid(x,y,z,rx,ry,rz,mat,name,sub=2):
    m=trimesh.creation.icosphere(subdivisions=sub,radius=1)
    m.apply_scale([rx,ry,rz]);m.apply_translation([x,y,z]);put(m,mat,name)

def disk(x,y,z,rx,rz,height,mat,name,sections=48):
    m=trimesh.creation.cylinder(radius=1,height=height,sections=sections)
    # Cylinder axis +Z; after rotation X=90, original height becomes world Y.
    m.apply_scale([rx,rz,1]);m.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[1,0,0]));m.apply_translation([x,y,z]);put(m,mat,name)

def curved_glass(x,y,z,rx,rz,height,name):
    """A curved wall made of genuine triangles, open top; UV-less transparent mesh."""
    n=48;verts=[];faces=[]
    for i in range(n+1):
        a=2*math.pi*i/n
        for h in [-height/2,height/2]:verts.append([x+rx*math.cos(a),y+h,z+rz*math.sin(a)])
    for i in range(n):
        j=i*2;faces.extend([(j,j+2,j+1),(j+1,j+2,j+3)])
    put(trimesh.Trimesh(vertices=np.array(verts),faces=np.array(faces),process=False), 'glass',name)

def sofa(x,z,prefix,mat='leather_light'):
    # Rounded upholstered volumes and seamed multi-seat cushions, not box-shaped sofas.
    for k in range(3):
        cx=x+(k-1)*1.18
        ellipsoid(cx,.52,z, .64,.22,.62,mat,prefix+'_individual_cushion',2)
        ellipsoid(cx,1.10,z+.58,.66,.48,.18,mat,prefix+'_cushioned_back',2)
        for off in (-.35,.34):
            pipe((cx+off,.62,z-.48),(cx+off,.64,z+.45),.006,'antique_copper',prefix+'_seam')
    for dx in (-1.86,1.86):
        ellipsoid(x+dx,.68,z,.23,.41,.78,mat,prefix+'_rounded_arm',2)
    for dx in (-1.5,1.5):
        for dz in (-.5,.49):pipe((x+dx,.05,z+dz),(x+dx,.31,z+dz),.05,'antique_gold',prefix+'_turned_leg',10)
    for dx in (-.74,.68):
        ellipsoid(x+dx,.98,z+.24,.40,.36,.17,'linen',prefix+'_embroidered_throw',2)

def armchair(x,z,prefix):
    ellipsoid(x,.54,z,.72,.25,.66,'velvet',prefix+'_upholstered_seat')
    ellipsoid(x,1.12,z+.53,.71,.55,.21,'velvet',prefix+'_curved_back')
    for dx in (-.67,.67):ellipsoid(x+dx,.68,z,.18,.34,.65,'velvet',prefix+'_rounded_arm',2)
    for dx in (-.49,.49):
        for dz in (-.40,.40):pipe((x+dx,.12,z+dz),(x+dx,.29,z+dz),.045,'antique_gold',prefix+'_leg')

def grand_v04(x,z,prefix):
    # Genuine extruded grand-piano outline in world-space, with an opening lid and keyboard.
    poly=[(-1.27,-.63),(.9,-.63),(1.35,-.34),(1.52,.08),(1.38,.58),(.89,.97),(-.65,1.05),(-1.23,.82)]
    T=trimesh.transformations.rotation_matrix(math.pi/2,[1,0,0]);T[:3,3]=[x,1.24,z]
    extrude_profile(poly,.25,'piano',prefix+'_body',T)
    for dx,dz in [(-.94,-.41),(.93,-.23),(.22,.76)]:
        pipe((x+dx,.07,z+dz),(x+dx,1.1,z+dz),.069,'ebony',prefix+'_curved_leg',14)
        disk(x+dx,.08,z+dz,.09,.09,.07,'antique_gold',prefix+'_caster')
    # Lip/rim follows piano silhouette with brass-finish narrow curved rail.
    for i in range(len(poly)):
        a=poly[i];b=poly[(i+1)%len(poly)]
        pipe((x+a[0],1.4,z+a[1]),(x+b[0],1.4,z+b[1]),.018,'antique_gold',prefix+'_gold_rim')
    # Angled opening lid, large dark glossy trapezoid (two-sided mesh), lid prop.
    verts=np.array([[x-1.20,1.49,z+.80],[x+1.25,2.43,z+.58],[x+1.37,2.35,z-.22],[x-1.22,1.52,z-.49]])
    mesh=trimesh.Trimesh(vertices=verts,faces=[[0,1,2],[0,2,3]],process=False)
    put(mesh,'piano',prefix+'_raised_lid')
    pipe((x+.35,1.37,z+.35),(x+.50,2.02,z+.35),.025,'antique_gold',prefix+'_lid_prop')
    # Strung harp visible under lid and over the body.
    disk(x+.15,1.45,z+.24,1.10,.58,.018,'antique_gold',prefix+'_inner_soundboard',56)
    for i in range(18):
        u=-.80+i*.09;pipe((x+u,1.469,z-.30),(x+u+.20,1.469,z+.60),.0028,'steel',prefix+'_piano_string',5)
    box(x-.17,1.23,z-.92,2.10,.18,.64,'piano',prefix+'_keybed')
    for i in range(36):
        cx=x-1.18+i*.058
        box(cx,1.34,z-1.03,.053,.035,.26,'vintage_white',prefix+'_white_key')
        if i%7 not in (2,6): box(cx+.029,1.38,z-.95,.029,.049,.15,'ebony',prefix+'_black_key')
    box(x-.12,.43,z-1.74,1.10,.18,.44,'grain_leather',prefix+'_piano_bench')
    for dx in (-.42,.42):pipe((x+dx,.07,z-1.74),(x+dx,.36,z-1.74),.056,'ebony',prefix+'_bench_leg')

def trumpet(x,y,z,room,slot,angle=0):
    T=tx_rot(x,y,z,angle)
    # Bell points diagonally: tapered cone + annulus and a connected winding brass tube.
    for a,b in [((-.27,-.2,0),(.19,-.2,0)),((.19,-.2,0),(.31,-.08,0)),((.31,-.08,0),(.27,.29,0)),((.27,.29,0),(-.30,.31,0)),((-.30,.31,0),(-.32,-.13,0))]:
        localpipe(a,b,.034,'gold_metal',f'interact_{room}_{slot}_trumpet',T,12)
    for u in (-.13,0,.13):
        localpipe((u,-.23,.042),(u,.39,.042),.022,'gold_metal','trumpet_valve',T,9)
        localbox(u,.36,.042,.078,.025,.08,'antique_gold','trumpet_button',T)
    bell=trimesh.creation.cone(radius=.18,height=.32,sections=28)
    bell.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[1,0,0]));bell.apply_translation([-.33,.32,0])
    bell.apply_transform(T);put(bell,'gold_metal',f'interact_{room}_{slot}_trumpet_bell')
    localpipe((.28,-.20,0),(.50,-.2,0),.035,'steel','trumpet_mouthpiece',T)

def clarinet(x,y,z,room,slot,angle=0):
    T=tx_rot(x,y,z,angle)
    localpipe((0,-.62,0),(0,.58,0),.051,'ebony',f'interact_{room}_{slot}_clarinet',T,14)
    for i in range(15):
        yy=-.50+i*.069
        localbox(((-1)**i)*.032,yy,.051,.061,.024,.013,'steel','clarinet_nickel_key',T)
    localpipe((0,.59,0),(.075,.78,0),.033,'ebony','clarinet_mouthpiece',T)
    cone=trimesh.creation.cone(radius=.10,height=.17,sections=18)
    cone.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[1,0,0]))
    cone.apply_translation([0,-.69,0]);cone.apply_transform(T);put(cone,'ebony','clarinet_flared_bell')

def floating_pendant(px,pz,kind,room):
    for i in range(11):
        a=i*math.pi*(3-math.sqrt(5))
        rad=.24+.17*math.sqrt(i)
        x=px+math.cos(a)*rad;z=pz+math.sin(a)*rad
        bottom=3.95+((i*3)%8)*.17
        pipe((x,5.74,z),(x,bottom+.26,z),.007,'antique_gold',room+'_cable',6)
        pipe((x,bottom+.28,z),(x,bottom,z),.033,'antique_gold',room+'_pendant')
        disk(x,bottom-.045,z,.070,.070,.025,'emissive_amber',room+'_led_tip',12)

ROOMS=('main','acoustic','electric','brass','strings')
for rid,kind in enumerate(ROOMS):
    zz=rid*23.5;label=f'room_{rid}_{kind}_v04';dark='espresso' if kind in ('electric','brass') else 'walnut'
    # Acoustically soft layered carpet: real textured floor mesh with brass inlays.
    plane(-2.7,.058,zz-2.6,10.6,10.7,'wool_detail',label+'_woven_carpet',10.7)
    for bx in (-8.10,8.10):
        pipe((bx,.16,zz-10.3),(bx,.16,zz+10.5),.021,'antique_gold',label+'_floor_brass_inlay')
    # Display niches are physically shallow alcoves: varied walnut side cheeks,
    # rear padded/travertine panels, LED reveals and actual shelves.
    for s in (-1,1):
        for j in range(6):
            z=zz-9.3+j*3.55
            box(s*9.37,2.9,z-1.44,.30,4.55,.075,dark,label+'_wall_bay_side')
            box(s*9.37,2.9,z+1.44,.30,4.55,.075,dark,label+'_wall_bay_side')
            box(s*9.49,3.01,z,.025,4.25,2.90,'cream_wall',label+'_wall_bay_fabric')
            box(s*9.34,4.93,z,.035,.10,2.8,'emissive_amber',label+'_niche_light')
            box(s*9.32,1.0,z,.23,.026,3.04,'antique_gold',label+'_niche_shelf')
        box(s*9.5,5.47,zz,.12,.09,22.2,'emissive_amber',label+'_architectural_cove_light')
        # Floor-level cabinets receive intricate fluting and drawer pulls.
        for j in range(18):
            z=zz-10.4+j*1.20
            box(s*9.18,.40,z,.055,.42,.07,'walnut_slat',label+'_wood_cabinet_reeded_panel')
    # A luminous cream coffered ceiling like the approved interior, not a
    # large unlit black plane. Recesses remain black between warmer panels.
    for cx in (-4.8,0,4.8):
        box(cx,5.65,zz,4.12,.035,20.7,'warm_cream',label+'_warm_ceiling_coffer')
        for side in (-2.01,2.01):
            box(cx+side,5.61,zz,.027,.07,20.6,'antique_gold',label+'_ceiling_coffer_brass')
    # Ceiling accent coffers and gold trim from actual meshes.
    for yx in (-7.7,7.7):
        box(yx,5.62,zz,.11,.11,22.2,'antique_gold',label+'_ceiling_border')
    for z in (zz-10.8,zz+10.8):box(0,5.58,z,17,.08,.06,'antique_gold',label+'_ceiling_coffer')
    # Double-sided central architectural plinth replaces the v03 rectangular box.
    disk(4.07,.36,zz+.20,2.30,1.50,.64,dark,label+'_oval_showcase_base')
    disk(4.07,.70,zz+.20,2.33,1.53,.065,'antique_gold',label+'_oval_brass_top')
    disk(4.07,.74,zz+.20,2.20,1.39,.035,'stone_detail',label+'_black_marble_showcase_top')
    for n in range(54):
        a=2*math.pi*n/54
        x=4.07+2.23*math.cos(a);z=zz+.20+1.43*math.sin(a)
        pipe((x,.10,z),(x,.62,z),.027,'antique_gold',label+'_fluted_showcase_panelling',6)
    curved_glass(4.07,2.01,zz+.20,2.25,1.50,2.46,label+'_real_curved_glass_case')
    disk(4.07,.045,zz+.20,2.40,1.60,.05,'emissive_amber',label+'_showcase_toekick')
    floating_pendant(4.07,zz+.20,kind,label)
    # Rich organic lounge grouping away from showroom navigation line.
    sofa(-3.65,zz-2.75,label+'_three_seat_sofa',mat='leather_light' if rid in (0,1) else 'leather_dark')
    armchair(-6.55,zz-4.55,label+'_boutique_armchair')
    disk(-3.66,.36,zz-4.75,1.23,.93,.17,'stone_detail',label+'_marble_round_table')
    disk(-3.66,.23,zz-4.75,1.07,.80,.24,'antique_gold',label+'_coffee_gold_pedestal')
    disk(-3.66,.08,zz-4.75,.94,.70,.06,'ebony',label+'_coffee_table_foot')
    disk(-2.65,.55,zz-4.75,.18,.18,.06,'antique_gold',label+'_table_bowl')
    # Articulated display frames and upper-level lounge/mezzanine feel.
    for sx in (-8.0,-5.8,6.8,8.0):
        box(sx,5.0,zz+8.3,.13,1.5,.12,'antique_gold',label+'_high_gallery_column')
    box(0,4.70,zz+8.9,8.5,.18,2.1,dark,label+'_mezzanine_shelf')
    for sx in np.linspace(-4.0,4.0,9):
        box(float(sx),5.12,zz+7.96,.026,.77,.04,'antique_gold',label+'_balcony_railing')
    box(0,5.4,zz+7.96,8.4,.035,.045,'antique_gold',label+'_handrail')
    # Layered feature panel at back: actual marble slab + brass-fluted ribs.
    # Keep the walk-through portal unobstructed at ground level.
    box(0,4.80,zz+9.95,4.1,1.42,.10,'stone_detail',label+'_upper_lobby_black_stone')
    for n in range(16):
        box(-2.0+n*.264,4.80,zz+9.88,.017,1.35,.022,'antique_gold',label+'_upper_feature_brass_slats')
    # Display desk and lush planters, with no flat photo imagery.
    box(-5.7,.80,zz+7.55,3.1,1.6,.85,'stone_detail',label+'_consultation_reception')
    box(-5.7,1.61,zz+7.55,3.15,.055,.93,'antique_gold',label+'_reception_edge')
    for px,pz in ((-7.1,zz+4.1),(7.7,zz+6.4)):
        disk(px,.26,pz,.43,.43,.53,'dark_marble',label+'_planter_pot',20)
        pipe((px,.51,pz),(px,2.72,pz),.08,'walnut',label+'_tree_stem')
        for n in range(17):
            ang=n*2.39996
            ellipsoid(px+.33*math.cos(ang),2.20+.48*math.cos(n),pz+.32*math.sin(ang),.24,.12,.13,'olive',label+'_olive_tree_leaves',1)
    # Room-specific grounded merchandise and fixtures.
    if kind=='electric':
        for a in range(4):
            xx=-8.0+a*1.48
            box(xx,.72,zz+5.40,1.18,1.25,.57,'black',label+'_boutique_guitar_amp')
            box(xx,.71,zz+5.10,1.00,.86,.045,'vinyl',label+'_speaker_grille')
            for dx in (-.44,.44):pipe((xx+dx,1.30,zz+5.06),(xx+dx,.25,zz+5.06),.014,'antique_gold',label+'_amp_side_rail')
            for k in range(6):disk(xx-.36+k*.14,1.36,zz+5.0,.025,.025,.013,'antique_gold',label+'_amp_knob',8)
    elif kind=='brass':
        for a in range(5):
            off=a-2
            trumpet(-4.4+off*.82,2.4,zz+5.20,rid,200+a,0)
            clarinet(-4.40+off*.74,2.30,zz+7.0,rid,230+a,0)
        box(-4.4,1.12,zz+5.32,5.9,.18,2.2,dark,label+'_brass_instrument_plinth')
        box(-4.4,1.25,zz+5.32,5.95,.055,2.24,'antique_gold',label+'_brass_display_plinth_rim')
    elif kind=='strings':
        # Main recital grand is actually geometrically shaped rather than an amp-sized box.
        grand_v04(-2.60,zz+3.10,label+'_hero_grand')
        plane(-2.60,.068,zz+2.5,5.2,6.1,'wool_detail',label+'_recital_carpet',6.1)
    elif kind=='acoustic':
        disk(-6.0,.70,zz+5.1,1.0,.75,.08,'stone_detail',label+'_consultation_table')
        for off in (-1.4,1.4):armchair(-6.0+off,zz+6.50,label+'_consultation_chair')

# GLTF camera looks toward +Z; unlike a conventional architect plan,
# positive x appears camera-left. Mirror the authored scene so the sofa is
# visually camera-left and central highlight island is on the right,
# reproducing the composition the client approved.
for geometry in scene.geometry.values():
    transform=np.diag([-1,1,1,1])
    geometry.apply_transform(transform)
# Export a full auditable GLB with real meshes and no image-plane room wallpaper.
OUT=ROOT/'assets/rooms/luxury-showroom-v04.glb'
scene.export(OUT)
check=trimesh.load(OUT,force='scene')
assert len(check.geometry)>1000
assert check.bounds[1,2]>100
assert not any('billboard' in n or 'picture_backdrop' in n for n in check.geometry)
print(f'v0.4 authored GLB {OUT} size={OUT.stat().st_size:,} meshes={len(check.geometry)}')