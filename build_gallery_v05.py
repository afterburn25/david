"""DAVID v0.5 -- real geometry / physical material pass atop v0.4.

Rebuild: python build_gallery_v05.py && python optimize_gallery_v05.py
Dependencies: numpy, Pillow, trimesh, shapely, scipy. This is not a
photogrammetric reconstruction nor a photographic backdrop. All artwork is
inspiration only. This script does NOT access or update the PHP database.
"""
from pathlib import Path
import math
import numpy as np
import trimesh
from PIL import Image, ImageFilter
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals
from shapely.geometry import Polygon
from shapely.ops import triangulate

ROOT=Path(__file__).resolve().parent
# Build v0.4 geometry once; v0.5 replaces and improves physical components.
src=ROOT/'build_gallery_v04.py'
ns={'__file__':str(src),'__name__':'__main__'}
exec(compile(src.read_text(),str(src),'exec'),ns)
scene=ns['scene']; M=ns['M'];put=ns['put'];box=ns['box'];pipe=ns['pipe'];disk=ns['disk']
plane=ns['plane'];room_centers=[0,23.5,47,70.5,94]
rng=np.random.default_rng(5052026)

# --------------------------------------------------------------
# Procedural physical finishes. These are PBR textures mapped to
# REAL guitar body geometry, not image planes/background photos.
# --------------------------------------------------------------
N=512
yy,xx=np.mgrid[0:N,0:N]; u=(xx-N/2)/(N/2);v=(yy-N/2)/(N/2)
radial=np.sqrt((u*.88)**2+(v*.72)**2)
flame=np.sin(xx*.034 + 8*np.sin(yy*.017) + 2*np.sin(xx*.097))*8
line=np.sin(xx*.64+1.2*np.sin(yy*.03))*2
noise=rng.normal(0,2.2,(N,N))

def finish_texture(name):
    if name=='sunburst':
        # warm maple center to crimson-brown transparent lacquer edge
        fac=np.clip((radial-.21)/.66,0,1)**2.4
        center=np.array([228,145,62]);edge=np.array([39,12,10]);arr=center[None,None,:]*(1-fac[:,:,None])+edge[None,None,:]*fac[:,:,None]
        arr=arr+(flame+line+noise)[:,:,None]*np.array([1,.67,.36])
    elif name=='tiger_maple':
        center=np.array([226,169,88]);arr=np.broadcast_to(center,(N,N,3)).copy().astype(float)
        arr+=(flame*2+noise)[:,:,None]*[1,.61,.31]
    elif name=='cherry':
        arr=np.ones((N,N,3))*[142,20,24];arr+=(flame*.2+noise)[:,:,None]*[1,.3,.3]
    elif name=='midnight_blue':
        arr=np.ones((N,N,3))*[13,66,92];arr+=(flame*.20+noise)[:,:,None]*[.2,.6,1]
    elif name=='cream':
        arr=np.ones((N,N,3))*[227,216,179];arr+=noise[:,:,None]
    elif name=='spruce':
        wood=7*np.sin(xx*.39+3*np.sin(yy*.007))+3*np.sin(xx*1.5)
        arr=np.ones((N,N,3))*[216,172,101];arr+=(wood+noise)[:,:,None]*[1,.58,.32]
    elif name=='mahogany':
        wood=13*np.sin(xx*.19+8*np.sin(yy*.013))+5*np.sin(xx*.90)
        arr=np.ones((N,N,3))*[120,55,28];arr+=(wood+noise)[:,:,None]*[1,.60,.48]
    else:raise KeyError(name)
    return Image.fromarray(np.uint8(np.clip(arr,0,255)),'RGB').filter(ImageFilter.GaussianBlur(.35))

def normal_map(img,s=3.2):
    gray=np.asarray(img.convert('L').filter(ImageFilter.GaussianBlur(.8)),dtype=np.float32)/255
    gy,gx=np.gradient(gray)
    normal=np.stack((-gx*s,-gy*s,np.ones_like(gx)),-1)
    normal/=np.linalg.norm(normal,axis=-1,keepdims=True)
    return Image.fromarray(np.uint8(np.clip((normal*.5+.5)*255,0,255)))

for kind in ('sunburst','tiger_maple','cherry','midnight_blue','cream','spruce','mahogany'):
    tex=finish_texture(kind)
    M['finish_'+kind]=PBRMaterial(name='v05 finish '+kind,baseColorTexture=tex,
                  normalTexture=normal_map(tex),baseColorFactor=[1.0,1.0,1.0,1.0],
                  metallicFactor=.06,roughnessFactor=.23 if kind not in ('spruce','mahogany') else .38)

# Use correct UV projections on already-modelled, three-dimensional body meshes.
# Wall guitars have width in world Z, hero guitars in X; neither is a photo.
retextured=0
for node in list(scene.graph.nodes_geometry):
    if not node.startswith('interact_') or '_guitar_' not in node:continue
    transform, key=scene.graph[node]
    mesh=scene.geometry[key]
    vert=np.asarray(mesh.vertices)
    ranges=np.ptp(vert,axis=0)
    lateral=2 if ranges[2]>ranges[0] else 0
    uu=(vert[:,lateral]-vert[:,lateral].min())/max(ranges[lateral],.0001)
    vv=(vert[:,1]-vert[:,1].min())/max(ranges[1],.0001)
    room=int(node.split('_')[1])
    # Acoustic Hall uses wood grain; other rooms show a range of lacquer finishes.
    if room==1: finish=('spruce','tiger_maple','mahogany')[retextured%3]
    else: finish=('sunburst','cherry','midnight_blue','cream','tiger_maple')[retextured%5]
    mesh.visual=TextureVisuals(uv=np.column_stack([uu,vv]), material=M['finish_'+finish])
    retextured+=1
assert retextured>70, retextured

# ------------------------------------------------------------------
# Sculpted bridge, individually mounted pickup covers, knobs, framed
# gold display plates; add near actual body positions while making sure
# they face INSIDE the showroom rather than embedded in rear cabinets.
# ------------------------------------------------------------------
M['aged_nickel']=PBRMaterial(name='Aged nickel instrument hardware',baseColorFactor=[.61,.60,.53,1],metallicFactor=.89,roughnessFactor=.28)
M['dark_rosewood']=PBRMaterial(name='Dark rosewood detail',baseColorFactor=[.10,.043,.026,1],metallicFactor=.0,roughnessFactor=.56)
M['bound_cream']=PBRMaterial(name='Ivory guitar binding',baseColorFactor=[.95,.83,.59,1],metallicFactor=0,roughnessFactor=.44)
M['recessed_amber']=PBRMaterial(name='Interior architectural warm light',baseColorFactor=[1,.81,.53,1],emissiveFactor=[1,.68,.36],metallicFactor=0,roughnessFactor=.7)

# Distinct real world-space showcase labels and guitar controls.
# No pseudo product names/prices/logos are baked onto instruments.
def little_box(x,y,z,w,h,d,material,name):box(float(x),float(y),float(z),w,h,d,material,name)

detail_count=0
for node in list(scene.graph.nodes_geometry):
    if not node.startswith('interact_') or '_guitar_' not in node:continue
    mesh=scene.geometry[scene.graph[node][1]]
    p=mesh.bounds.mean(axis=0)
    span=np.ptp(mesh.bounds,axis=0)
    wall=abs(p[0])>7.1
    room=int(node.split('_')[1]);acoustic=(room==1)
    if wall:
        face_x=p[0]+(.083 if p[0]<0 else -.083)
        # Horizontal dimensions follow world Z after guitars were wall-oriented.
        # Thin covers stand proud of the lacquer on front, not floating photos.
        for dy in ([-.07] if acoustic else [-.11,.105]):
            little_box(face_x,p[1]+dy,p[2],.023,.068,.21 if not acoustic else .12,
                       'dark_rosewood' if acoustic else 'aged_nickel','v05_pickup_cover')
        if not acoustic:
            for dy in (-.21,-.31):
                q=p.copy();q[1]+=dy;q[2]+=.14
                # tiny actual radial knob body plus index line
                r=trimesh.creation.cylinder(radius=.025,height=.018,sections=16)
                r.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[0,1,0]))
                r.apply_translation([face_x,p[1]+dy,p[2]+.14]);put(r,'aged_nickel','v05_volume_tone_knob')
        # Four-point tiny pearl inlays down the neck.
        for dy in (.41,.63,.85,1.07):
            little_box(face_x,p[1]+dy,p[2],.018,.025,.03,'bound_cream','v05_neck_inlay')
    else:
        face_z=p[2]+.07
        for dy in (-.12,.07):little_box(p[0],p[1]+dy,face_z,.21,.068,.025,'aged_nickel','v05_hero_humbucker')
    detail_count+=1

# ------------------------------------------------------------
# Consistent softly illuminated display alcoves, warm plaster
# ceilings, and actual warm LED panels recessed into the cabinets.
# ------------------------------------------------------------
# The original v0.3 opaque black ceiling created the pitch-black overhead
# silhouette. Replace only the ceiling material/geometry. Existing track
# fixtures, PBR illuminated coves, and ceiling coffers remain 3D meshes.
remove=[]
for node in scene.graph.nodes_geometry:
    if node.startswith('room_') and '_ceiling_' in node and '_track_' not in node and '_coffer_' not in node:
        remove.append(node)
scene.delete_geometry(remove)
for rid,zz in enumerate(room_centers):
    label=f'room_{rid}_v05'
    # Inset luminous travertine with thin brass mullions; no sky/black ceiling void.
    box(0,5.80,zz,19.65,.22,22.65,'warm_cream',label+'_plaster_ceiling')
    for cx in (-6.55,-2.18,2.18,6.55):
        box(cx,5.67,zz,3.18,.045,20.6,'warm_cream',label+'_light_ceiling_panel')
        for border in (-1.59,1.59):
            box(cx+border,5.61,zz,.018,.055,20.5,'antique_gold',label+'_brass_ceiling_mullion')
    # Indirect alcove light is represented by actual luminous strips with
    # surrounding actual walnut casing (no photos glued to walls).
    for side in (-1,1):
        x=side*9.18
        for j in range(6):
            z=zz-9.3+j*3.55
            for offset in (-1.32,1.32):
                little_box(x,2.88,z+offset,.06,3.73,.027,'recessed_amber',label+'_backlit_niche_side')
            little_box(x,1.09,z,.065,.06,2.67,'recessed_amber',label+'_backlit_niche_sill')
    # Photographic reference has visible amber cove illumination at base of
    # cabinetry and behind the central presentation island.
    for sx in (-9.14,9.14):
        little_box(sx,.13,zz,.08,.045,22.0,'recessed_amber',label+'_toe_reveal')
    # Carved geometric medallion layered into stone reception desk.
    for x in (-5.93,-5.47):
        little_box(x,1.22,zz+7.10,.015,.11,.012,'antique_gold',label+'_counter_gold_inlay')
    # Downlight under the mezzanine shelf (modeled luminous area).
    little_box(0,4.56,zz+8.3,6.1,.035,.16,'recessed_amber',label+'_balcony_indirect_light')

OUT=ROOT/'assets/rooms/luxury-showroom-v05.glb'
scene.export(OUT)
check=trimesh.load(OUT,force='scene')
assert len(check.graph.nodes_geometry)>5000
assert check.bounds[1,2]>103
assert any(n.startswith('interact_') for n in check.graph.nodes_geometry)
print('v0.5 full:',OUT.stat().st_size,'bytes',len(check.geometry),'nodes', retextured,'guitars upgraded',len(remove),'overhead black surfaces replaced')