"""DAVID v0.3 physically-modeled five-gallery showroom.
Authored 3D geometry with PBR materials; reference photographs are NOT textures/backdrops.
Run: python build_gallery_v03.py (requires trimesh, numpy, pillow, shapely, scipy).
"""
from __future__ import annotations
from pathlib import Path
import math, os, random
import numpy as np
import trimesh
from PIL import Image, ImageFilter
from shapely.geometry import Polygon
from shapely.ops import triangulate
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'assets' / 'rooms' / 'luxury-showroom-v03.glb'
OUT.parent.mkdir(parents=True, exist_ok=True)
scene = trimesh.Scene()
SEED=8137
rng=np.random.default_rng(SEED)
count=0
M={
 'walnut':PBRMaterial(name='American walnut satin',baseColorFactor=[.25,.13,.077,1],metallicFactor=0,roughnessFactor=.61),
 'espresso':PBRMaterial(name='Espresso wood',baseColorFactor=[.105,.062,.042,1],metallicFactor=.03,roughnessFactor=.55),
 'brass':PBRMaterial(name='Brushed architectural brass',baseColorFactor=[.77,.54,.26,1],metallicFactor=.8,roughnessFactor=.27),
 'warm_led':PBRMaterial(name='Warm architectural lighting',baseColorFactor=[1,.77,.41,1],emissiveFactor=[1,.49,.19],metallicFactor=.1,roughnessFactor=.38),
 'ivory':PBRMaterial(name='Cream plaster',baseColorFactor=[.72,.60,.49,1],metallicFactor=0,roughnessFactor=.89),
 'glass':PBRMaterial(name='Showcase glass',baseColorFactor=[.58,.71,.76,.17],alphaMode='BLEND',doubleSided=True,metallicFactor=.18,roughnessFactor=.07),
 'piano':PBRMaterial(name='Piano lacquer',baseColorFactor=[.025,.025,.03,1],metallicFactor=.16,roughnessFactor=.14),
 'vinyl':PBRMaterial(name='Amplifier textile',baseColorFactor=[.08,.08,.08,1],metallicFactor=0,roughnessFactor=.95),
 'leather':PBRMaterial(name='Italian cognac leather',baseColorFactor=[.19,.105,.065,1],metallicFactor=0,roughnessFactor=.65),
 'cushion':PBRMaterial(name='Linen upholstery',baseColorFactor=[.40,.37,.31,1],metallicFactor=0,roughnessFactor=.97),
 'bronze':PBRMaterial(name='Copper bronze',baseColorFactor=[.41,.22,.11,1],metallicFactor=.55,roughnessFactor=.32),
 'black':PBRMaterial(name='Charcoal metal',baseColorFactor=[.045,.051,.054,1],metallicFactor=.50,roughnessFactor=.45),
 'steel':PBRMaterial(name='Chrome',baseColorFactor=[.62,.65,.66,1],metallicFactor=.92,roughnessFactor=.20),
 'red':PBRMaterial(name='Cherry guitar lacquer',baseColorFactor=[.53,.038,.045,1],metallicFactor=.20,roughnessFactor=.22),
 'amber':PBRMaterial(name='Amber guitar lacquer',baseColorFactor=[.75,.33,.065,1],metallicFactor=.15,roughnessFactor=.24),
 'teal':PBRMaterial(name='Teal guitar lacquer',baseColorFactor=[.027,.25,.3,1],metallicFactor=.22,roughnessFactor=.22),
 'cream':PBRMaterial(name='Vintage cream guitar',baseColorFactor=[.76,.66,.49,1],metallicFactor=.17,roughnessFactor=.31),
 'leaf':PBRMaterial(name='Plant leaf',baseColorFactor=[.075,.19,.074,1],metallicFactor=0,roughnessFactor=.97),
 'wood_instrument':PBRMaterial(name='Maple violin',baseColorFactor=[.56,.21,.08,1],metallicFactor=.04,roughnessFactor=.25),
}

def mktex(kind, N=384):
 rr=np.random.default_rng(282+len(kind))
 yy,xx=np.indices((N,N)); noise=rr.normal(0,1,(N,N));
 if kind=='carpet':
  mottled=rr.normal(0,17,(N,N)); stripes=8*np.sin(xx*.085+rr.normal(0,.25,(N,N)))
  a=np.stack([113+mottled+stripes,103+mottled+stripes,96+mottled+stripes],axis=-1)
 elif kind=='rug':
  # Low-contrast irregular wool weave rather than banded synthetic stripes.
  coarse=rr.normal(0,1,(28,28));coarse=np.asarray(Image.fromarray(np.uint8(np.clip(coarse*25+128,0,255))).resize((N,N),Image.Resampling.BICUBIC)).astype(float)-128
  mar=rr.normal(0,5.5,(N,N)); organic=coarse*.70+7*np.sin(xx*.017+2*np.sin(yy*.014))
  a=np.stack([146+organic+mar,136+organic+mar,124+organic+mar],axis=-1)
 elif kind=='wood':
  grain=21*np.sin((xx+rr.normal(0,1,(N,N))*3)*.08+6*np.sin(yy*.023)) + 12*np.sin(xx*.42)
  a=np.stack([104+grain,59+grain*.64,33+grain*.43],axis=-1)
 elif kind=='marble':
  v=27*np.sin(xx*.037+yy*.009+8*np.sin(yy*.031))+9*noise
  a=np.stack([43+v,38+v*.94,34+v*.91],axis=-1)
 elif kind=='wall':
  v=rr.normal(0,5,(N,N)); a=np.stack([128+v,105+v,83+v],axis=-1)
 elif kind=='leather':
  v=rr.normal(0,7,(N,N));a=np.stack([95+v,50+v*.7,30+v*.65],axis=-1)
 else: raise ValueError(kind)
 return Image.fromarray(np.uint8(np.clip(a,0,255)),'RGB').filter(ImageFilter.GaussianBlur(.3))

for k in ('carpet','rug','wood','marble','wall','leather'):
 factor={'carpet':.86,'rug':.96,'wood':.78,'marble':.76,'wall':.8,'leather':.72}[k]
 M[k]=PBRMaterial(name=f'Generated {k} PBR texture',baseColorTexture=mktex(k),baseColorFactor=[factor,factor,factor,1],metallicFactor=.2 if k=='marble' else 0,roughnessFactor=.22 if k=='marble' else .81)


def put(m,material,name,UV=None):
 global count
 if UV is None:
  # Basic shapes use PBR material without an image texture.
  m.visual=TextureVisuals(uv=np.zeros((len(m.vertices),2)),material=M[material] if isinstance(material,str) else material)
 else:
  m.visual=TextureVisuals(uv=np.asarray(UV),material=M[material] if isinstance(material,str) else material)
 scene.add_geometry(m,node_name=f'{name}_{count:05}',geom_name=f'{name}_{count:05}')
 count+=1
 return m

def box(x,y,z,w,h,d,material,name='architectural'): 
 m=trimesh.creation.box(extents=(w,h,d));m.apply_translation((x,y,z));put(m,material,name)

def plane(x,y,z,w,d,material,name,scale=2):
 verts=np.array([[x-w/2,y,z-d/2],[x+w/2,y,z-d/2],[x+w/2,y,z+d/2],[x-w/2,y,z+d/2]])
 faces=np.array([[0,2,1],[0,3,2]])
 uv=np.array([[0,0],[w/scale,0],[w/scale,d/scale],[0,d/scale]])
 put(trimesh.Trimesh(vertices=verts,faces=faces,process=False),material,name,uv)

def orb(x,y,z,r,mat,name='detail',sub=1,s=(1,1,1)):
 m=trimesh.creation.icosphere(subdivisions=sub,radius=r);m.apply_scale(s);m.apply_translation([x,y,z]);put(m,mat,name)

def pipe(a,b,r,mat,name='trim',segments=8):
 a=np.asarray(a,dtype=float);b=np.asarray(b,dtype=float);v=b-a;ln=np.linalg.norm(v)
 if ln<=1e-5:return
 m=trimesh.creation.cylinder(radius=r,height=ln,sections=segments)
 m.apply_transform(trimesh.geometry.align_vectors([0,0,1],v/ln));m.apply_translation((a+b)/2);put(m,mat,name)

def extrude_profile(points,thickness,material,name,transform=None):
 """True concave outline extrusion via polygon triangulation; front/back + sidewalls."""
 poly=Polygon(points)
 if not poly.is_valid:poly=poly.buffer(0)
 coords=list(poly.exterior.coords)[:-1]
 verts=[];faces=[];mapping={}
 def ix(t):
  k=tuple(round(float(a),5) for a in t)
  if k not in mapping: mapping[k]=len(verts);verts.append(t)
  return mapping[k]
 for tri in triangulate(poly):
  if not poly.covers(tri.representative_point()):continue
  points2=list(tri.exterior.coords)[:-1]
  for j,zdir in enumerate([1,-1]):
   vs=[ix((pt[0],pt[1],zdir*thickness/2)) for pt in points2]
   faces.append(vs if zdir==1 else vs[::-1])
 for i,p in enumerate(coords):
  q=coords[(i+1)%len(coords)];a=ix((p[0],p[1],thickness/2));b=ix((q[0],q[1],thickness/2));c=ix((q[0],q[1],-thickness/2));d=ix((p[0],p[1],-thickness/2))
  faces.extend([(a,b,c),(a,c,d)])
 mesh=trimesh.Trimesh(vertices=np.array(verts),faces=np.array(faces),process=False)
 if transform is not None:mesh.apply_transform(transform)
 put(mesh,material,name)
 return mesh

def tx_rot(x,y,z,angle):
 t=trimesh.transformations.rotation_matrix(angle,[0,1,0]);t[:3,3]=(x,y,z);return t

def transform_prim(m,T,material,name):
 m.apply_transform(T);put(m,material,name)

def localbox(x,y,z,w,h,d,mat,name,T):
 m=trimesh.creation.box(extents=(w,h,d));m.apply_translation((x,y,z));transform_prim(m,T,mat,name)

def localpipe(a,b,r,mat,name,T,seg=8):
 a=np.asarray(a,float);b=np.asarray(b,float);v=b-a;ln=np.linalg.norm(v)
 if ln<1e-5:return
 m=trimesh.creation.cylinder(radius=r,height=ln,sections=seg)
 m.apply_transform(trimesh.geometry.align_vectors([0,0,1],v/ln));m.apply_translation((a+b)/2);transform_prim(m,T,mat,name)

ELECTRIC=[(-.17,-.48),(-.32,-.39),(-.39,-.18),(-.35,.00),(-.2,.15),(-.34,.28),(-.34,.41),(-.13,.33),(-.05,.17),(.08,.20),(.22,.46),(.32,.43),(.31,.21),(.22,.08),(.37,-.08),(.38,-.29),(.27,-.46),(.05,-.51)]
ACOUSTIC=[(-.1,-.54),(-.33,-.46),(-.43,-.26),(-.4,-.06),(-.24,.06),(-.18,.24),(-.28,.4),(-.19,.50),(0,.52),(.19,.50),(.28,.4),(.18,.24),(.24,.06),(.4,-.06),(.43,-.26),(.33,-.46),(.1,-.54)]
VIOLIN=[(-.11,-.39),(-.2,-.30),(-.23,-.18),(-.13,-.08),(-.20,.07),(-.24,.23),(-.11,.30),(0,.2),(.11,.3),(.24,.23),(.20,.07),(.13,-.08),(.23,-.18),(.2,-.3),(.11,-.39)]

def guitar(x,y,z,mat='red',acoustic=False,room=0,slot=0,angle=0):
 T=tx_rot(x,y,z,angle)
 outline=ACOUSTIC if acoustic else ELECTRIC
 # scale body to 1m high; headstock + neck adds another meter.
 pts=[(a,b) for a,b in outline]
 extrude_profile(pts,.105,mat,f'interact_{room}_{slot}_guitar',T)
 localbox(0,.76,.012,.103,.87,.085,'walnut','guitar_neck',T)
 localbox(0,.78,.067,.088,.84,.009,'black','guitar_fretboard',T)
 head=[(-.06,1.19),(.07,1.19),(.13,1.5),(.05,1.59),(-.09,1.55)]
 extrude_profile(head,.075,'walnut','guitar_headstock',T)
 for k in range(15):
  v=.41+k*.057;localbox(0,v,.079,.088,.005,.01,'brass','fret',T)
 for k in range(6):
  u=(k-2.5)*.013
  localpipe((u,-.34,.083),(u,1.48,.087),.0018,'steel','string',T,5)
  localpipe(((-1)**k*.08,1.27+k*.041,0),(0,1.23+k*.046,0),.012,'steel','guitar_tuner',T,6)
 if acoustic:
  # Soundhole is an actual circular recessed insert on the top face.
  m=trimesh.creation.cylinder(radius=.105,height=.003,sections=28)
  m.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[1,0,0]));m.apply_translation([0,.06,.060]);transform_prim(m,T,'black','guitar_soundhole')
  localbox(0,-.32,.082,.16,.04,.028,'walnut','guitar_bridge',T)
 else:
  localbox(0,-.03,.077,.21,.075,.032,'cream','guitar_pickup',T)
  localbox(0,-.23,.078,.22,.065,.025,'steel','guitar_bridge',T)
  for yy in (-.15,.01):orb(*((T@np.array([.22,yy,.088,1]))[:3]),.019,'steel','control_knob',1)

def strings_instrument(x,y,z,room,slot,angle):
 T=tx_rot(x,y,z,angle)
 extrude_profile(VIOLIN,.095,'wood_instrument',f'interact_{room}_{slot}_violin',T)
 localbox(0,.47,.01,.085,.42,.07,'walnut','violin_neck',T)
 orb(*((T@np.array([0,.77,0,1]))[:3]),.10,'wood_instrument','scroll',1)
 localbox(0,-.08,.075,.18,.03,.018,'walnut','violin_bridge',T)
 for k in range(4):localpipe(((k-1.5)*.017,-.29,.067),((k-1.5)*.017,.77,.065),.002,'steel','violin_string',T,5)

def brass_instrument(x,y,z,room,slot,angle):
 # Sculpted saxophone-like horn: curved neck, tapered bell, separate keys; oriented to face aisle.
 T=tx_rot(x,y,z,angle)
 pts=[(0,.66,0),(.08,.68,0),(.17,.51,0),(.16,.25,0),(.10,.10,0),(-.02,-.12,0),(-.02,-.31,0),(.08,-.40,0)]
 for a,b in zip(pts,pts[1:]):localpipe(a,b,.031,'brass',f'interact_{room}_{slot}_sax',T,10)
 m=trimesh.creation.cone(radius=.18,height=.33,sections=20)
 m.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
 m.apply_translation([.08,-.52,0]);transform_prim(m,T,'brass',f'interact_{room}_{slot}_sax_bell')
 for i in range(8):
  pt=(.13,.31-i*.069,.037);localbox(pt[0],pt[1],pt[2],.11,.035,.025,'steel','sax_key',T)

def grand_piano(x,z,room,slot):
 # Irregular piano footprint and elevated open lid with black lacquer and exposed brass frame.
 shape=[(-1.5,-.66),(.7,-.66),(1.45,-.38),(1.65,.12),(1.3,.80),(.2,1.05),(-1.5,.87)]
 # Body footprint x-z, extrude along y by composing XY then rotate about X 90 deg.
 m=trimesh.creation.box(extents=(2.8,.30,1.7));m.apply_translation((x,1.22,z));put(m,'piano',f'interact_{room}_{slot}_grand_piano')
 for dx,dz in ((-1.14,-.64),(1.02,-.35),(.45,.68)):
  pipe((x+dx,.10,z+dz),(x+dx,1.07,z+dz),.075,'black','piano_leg',12)
 # Open lid rotated up along spine, triangular dark plane in world coordinates
 verts=np.array([[x-1.25,1.35,z+.72],[x+1.3,1.95,z+.62],[x+1.2,2.04,z-.62],[x-1.25,1.39,z-.62]])
 put(trimesh.Trimesh(vertices=verts,faces=[[0,1,2],[0,2,3]],process=False),'piano','piano_lid')
 box(x,1.13,z-.95,2.65,.09,.54,'black','piano_keyboard_rail')
 for i in range(25):box(x-1.24+i*.102,1.18,z-1.10,.09,.025,.20,'cream','ivory_piano_key')
 box(x-.25,.48,z-1.78,1,.15,.48,'leather','piano_bench')

ROOMS=('main','acoustic','electric','brass','strings')
# World +z goes deeper into store. Zero entrance at z=-12, five galleries sequentially.
for idx,kind in enumerate(ROOMS):
 z=idx*23.5;room=f'room_{idx}_{kind}'
 dark='espresso' if kind in ('electric','brass') else 'walnut'
 box(0,-.18,z,20,.34,23.0,'espresso',room+'_floor_base')
 plane(0,.005,z,19.8,22.7,'wood',room+'_wood_floor',1.7)
 plane(-1.7,.039,z-1.9,8.8,8.6,'rug',room+'_patterned_lounge_rug',1.5)
 plane(4.5,.035,z+5.7,7.6,6.2,'carpet',room+'_gallery_carpet',1.7)
 # Architectural ceiling and dark feature slats
 box(0,5.88,z,20,.24,23,dark,room+'_ceiling')
 for x in (-8.8,-5.8,-2.8,0,2.8,5.8,8.8):
  box(x,5.73,z,.13,.29,22.3,'black',room+'_track_light_trough')
  for iz in range(7):
   zz=z-9.6+iz*3.1
   box(x,5.52,zz,.08,.075,.20,'warm_led',room+'_recessed_downlight')
 for side in (-1,1):
  sx=side*9.84
  box(sx,2.87,z,.32,5.9,23,dark,room+'_wall')
  # Six real recessed instrument cabinets per side; dark reveal and LED trim create illusion of depth.
  for k in range(6):
   zz=z-9.3+k*3.55
   box(side*9.55,2.80,zz,.23,4.7,3.10,'ivory',room+'_display_bay_back')
   for wallrim in (-1.53,1.53):
    box(side*9.26,2.84,zz+wallrim,.12,4.8,.10,'brass',room+'_vertical_brass_trim')
   box(side*9.26,5.18,zz,.10,.12,3.09,'warm_led',room+'_cabinet_led_top')
   box(side*9.25,.42,zz,.58,.84,3.17,dark,room+'_lower_cabinet')
   box(side*9.24,.86,zz,.59,.06,3.13,'brass',room+'_cabinet_rail')
   for j in range(12):
    box(side*9.00,.48,zz-1.43+j*.26,.055,.68,.026,'brass',room+'_cabinet_fluting')
   # Instruments occupy front of bay facing center aisle. Local +Z rotated into +/-X.
   ang=(math.pi/2 if side<0 else -math.pi/2)
   for slot,off in enumerate((-.61,.67)):
    xx=side*8.99
    if kind=='brass':brass_instrument(xx,2.62,zz+off,idx,k*2+slot,ang)
    elif kind=='strings':strings_instrument(xx,2.7,zz+off,idx,k*2+slot,ang)
    else:
     mat=('amber' if kind=='acoustic' else ['red','cream','teal','amber'][((k+slot)+idx)%4])
     guitar(xx,2.50,zz+off,mat,kind=='acoustic',idx,k*2+slot,ang)
  # walnut fluted end columns and brass skirting
  box(side*9.4,.10,z,.14,.14,22.4,'brass',room+'_wall_base_led')
  for columnZ in (z-11,z+11):
   box(side*9.31,2.9,columnZ,.34,5.75,.31,'brass',room+'_column')
 # lobby lounge furniture, physical geometry
 box(-3.15,.33,z-2.4,3.8,.43,1.32,'leather',room+'_sofa_seat')
 # Rounded leather seat volume keeps silhouettes soft, unlike cuboid placeholder furniture.
 orb(-3.15,.55,z-2.46,.69,'leather',room+'_rounded_seat',2,(2.56,.37,1.05))
 box(-3.15,.94,z-1.84,3.8,.87,.26,'leather',room+'_sofa_back')
 for side in (-1,1): box(-3.15+side*1.78,.64,z-2.4,.26,.64,1.37,'leather',room+'_sofa_arm')
 for i in (-1,0,1):box(-3.15+i*1.09,.82,z-2.38,.70,.28,.46,'cushion',room+'_sofa_pillow')
 box(-2.7,.32,z-4.34,2.10,.11,1.17,'marble',room+'_marble_coffee_table')
 for dx in (-.73,.73):pipe((-2.7+dx,0,z-4.34),(-2.7+dx,.27,z-4.34),.07,'brass',room+'_coffee_table_legs')
 box(-6.2,.42,z-4.4,1.2,.50,1.13,'leather',room+'_lounge_chair')
 box(-6.2,.81,z-3.99,1.2,.71,.25,'leather',room+'_chair_back')
 # center feature display pedestal glass and brass detail
 box(4.10,.36,z+.25,3.80,.56,2.45,dark,room+'_island_base')
 for i in range(21):box(2.35+i*.174,.35,z-1.01,.035,.49,.041,'brass',room+'_island_vertical_rib')
 for x in (2.22,5.98):
  for zz in (z-1.1,z+1.53):
   pipe((x,.62,zz),(x,3.22,zz),.022,'brass',room+'_glass_case_frame')
 # Transparent world-space GLB glass enclosure; not a photograph or CSS effect.
 box(4.10,1.93,z-1.10,3.50,2.55,.016,'glass',room+'_showcase_front_glass')
 box(4.10,1.93,z+1.45,3.50,2.55,.016,'glass',room+'_showcase_back_glass')
 for sideX in (2.32,5.90):
  box(sideX,1.93,z+.18,.016,2.55,2.54,'glass',room+'_showcase_side_glass')
 if kind in ('main','acoustic','electric'):
  for k,m in enumerate(('red','teal','amber')):
   guitar(3.08+k*.96,1.98,z+.2,m,kind=='acoustic',idx,100+k,0)
 elif kind=='brass':
  for k in range(3):brass_instrument(3.3+k*.82,2.04,z+.23,idx,100+k,0)
 elif kind=='strings':
  grand_piano(3.5,z+.2,idx,100)
 # Cylindrical pendant fixtures and golden lamp tips.
 for j in range(15):
  a=j*2.4;radius=.62+((j%3)*.13);x=4.15+math.cos(a)*radius;zz=z+math.sin(a)*radius
  pipe((x,5.6,zz),(x,4.1+.11*(j%4),zz),.012,'brass',room+'_pendant_stem')
  pipe((x,4.12+.11*(j%4),zz),(x,3.96+.11*(j%4),zz),.03,'warm_led',room+'_pendant_bulb')
 # leafy plants in real spatial positions, not photos
 for px,pz in ((-7.2,z+6.3),(7.2,z-7.3)):
  box(px,.35,pz,.7,.7,.7,'bronze',room+'_planter')
  pipe((px,.5,pz),(px,2.8,pz),.057,'walnut',room+'_planter_trunk')
  for j in range(8):
   a=j*2.42;orb(px+math.cos(a)*.38,2.40+math.cos(j)*.31,pz+math.sin(a)*.4,.39,'leaf',room+'_plant_leaves',1,(.9,1.2,.85))
 # Open multi-room walk-through on +z side. Portal jambs and lintel instead of walls.
 if idx<4:
  border=z+11.72
  for sx in (-6.22,6.22):
   box(sx,2.82,border,7.56,5.65,.35,dark,room+'_portal_dividing_wall')
   box(sx/abs(sx)*2.43,2.55,border,.18,5.11,.39,'brass',room+'_portal_inner_jamb')
  box(0,5.37,border,5.0,.96,.35,dark,room+'_portal_lintel')
  box(0,4.88,border,5.0,.045,.36,'warm_led',room+'_portal_led')

scene.export(OUT)
loaded=trimesh.load(OUT,force='scene')
assert len(loaded.graph.nodes_geometry)>200
assert os.path.getsize(OUT)>500_000
print(f'Generated: {OUT} bytes={OUT.stat().st_size} nodes={len(loaded.graph.nodes_geometry)} bounds={loaded.bounds.tolist()}')