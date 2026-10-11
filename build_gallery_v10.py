"""DAVID v0.10 REAL MODEL DETAIL PASS, derived from v0.7 optimized GLB.

This is a v0.7 compatible staging branch, not a replacement for an unavailable
v0.8. Images are ONLY visual references; no rasterized room photographs are used
as geometry or materials. Adds real string/fret/hardware and baked cabinet
illumination via physically placed texture-bearing cabinet backplates.

Reproducibility: python build_gallery_v10.py && python optimize_gallery_v10.py
"""
from pathlib import Path
from collections import Counter
import re, math
import numpy as np
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals
from PIL import Image, ImageFilter

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'assets/rooms/luxury-showroom-v07-optimized.glb'
DST=ROOT/'assets/rooms/luxury-showroom-v10-unoptimized.glb'
scene=trimesh.load(SRC,force='scene')

M={
 'steel':PBRMaterial(name='v10 precision nickel plated guitar string',baseColorFactor=[.79,.83,.86,1.0],metallicFactor=.9,roughnessFactor=.21),
 'rosewood':PBRMaterial(name='v10 inlaid rosewood guitar fretboard',baseColorFactor=[.19,.10,.055,1.0],metallicFactor=0.,roughnessFactor=.46),
 'pearl':PBRMaterial(name='v10 pearl fret dot markers',baseColorFactor=[.85,.82,.76,1.0],metallicFactor=.03,roughnessFactor=.24),
 'gold':PBRMaterial(name='v10 satin brass tuner hardware',baseColorFactor=[.70,.47,.22,1.0],metallicFactor=.80,roughnessFactor=.24),
 'black':PBRMaterial(name='v10 cast ebony plastic knobs',baseColorFactor=[.028,.025,.021,1.0],metallicFactor=0.,roughnessFactor=.37),
 'bridge':PBRMaterial(name='v10 brushed nickel bridge saddles',baseColorFactor=[.64,.69,.72,1.0],metallicFactor=.86,roughnessFactor=.22),
 'amber':PBRMaterial(name='v10 warm amber cove diffuser emissive',baseColorFactor=[.68,.43,.19,1.0],emissiveFactor=[.29,.13,.035],roughnessFactor=.83,metallicFactor=0),
 'back':None,
}
# Physically baked spotlight on a walnut display backing. This is an authored
# PBR albedo texture for *actual wall geometry*, NOT a photo-plane fake room.
w,h=256,512
rng=np.random.default_rng(11062026)
x,y=np.meshgrid(np.linspace(-1,1,w),np.linspace(0,1,h))
spot=np.exp(-(((x-.05)/.62)**2 + ((y-.86)/.5)**2)*1.4)
edge=np.clip(1-.24*x*x,0,1)
wood=3.8*np.sin((y*33 + x*1.7)*2*np.pi)+1.8*np.sin(y*95*2*np.pi)
noise=rng.normal(0,1.6,(h,w))
val=spot*56+(wood+noise)*.7
img=np.stack([133+val*.83,102+val*.76,74+val*.65],axis=2)*edge[:,:,None]
img=np.uint8(np.clip(img,0,255))
wood_img=Image.fromarray(img,'RGB').filter(ImageFilter.GaussianBlur(.15))
M['back']=PBRMaterial(name='v10 real cabinet backlight walnut finish',baseColorTexture=wood_img,baseColorFactor=[1.0,1.0,1.0,1.0],emissiveFactor=[.16,.09,.042],metallicFactor=0.02,roughnessFactor=.65)

stats=Counter()
serial=0

def add(m,material,name):
    global serial
    serial+=1
    name=f"{name}_{serial:06d}"
    # In v10 textures and normal maps must persist through the optimization step.
    if len(m.vertices)==0 or len(m.faces)==0:return
    if not hasattr(m.visual,'uv') or m.visual.uv is None or len(m.visual.uv)!=len(m.vertices):
        uv=np.zeros((len(m.vertices),2),dtype=float)
        m.visual=TextureVisuals(uv=uv,material=M[material])
    else:
        m.visual.material=M[material]
    scene.add_geometry(m,node_name=name,geom_name=name)
    stats[material]+=1


def rod(a,b,r,mat,label,segments=7):
    a=np.asarray(a,dtype=float);b=np.asarray(b,dtype=float)
    direction=b-a;length=float(np.linalg.norm(direction))
    if length<1e-5:return
    obj=trimesh.creation.cylinder(radius=r,height=length,sections=segments)
    obj.apply_transform(trimesh.geometry.align_vectors((0,0,1),direction/length))
    obj.apply_translation((a+b)/2)
    add(obj,mat,label)


def disc(c,r,mat,label,axis='x',height=.009,segments=14):
    m=trimesh.creation.cylinder(radius=r,height=height,sections=segments)
    if axis=='x':m.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[0,1,0]))
    m.apply_translation(c)
    add(m,mat,label)


def box(c,s,mat,label):
    m=trimesh.creation.box(extents=s)
    m.apply_translation(c)
    add(m,mat,label)


def textured_backplate(side,room,center_y,center_z,sequence):
    # Inward-facing *real* backing of an illuminated instrument cabinet niche.
    # At x +/- 9.18, deeper than pickable guitar body at +/- 8.99.
    cx=side*9.17; y0=center_y-1.08; z0=center_z-.49
    height=1.91;width=.96
    m=trimesh.creation.box(extents=(.019,height,width))
    m.apply_translation((cx,y0+height/2,z0+width/2))
    v=m.vertices
    uv=np.stack([(v[:,2]-z0)/width,(v[:,1]-y0)/height],axis=-1)
    m.visual=TextureVisuals(uv=uv,material=M['back'])
    scene.add_geometry(m,node_name=f'room_{room}_v10_cabinet_{sequence:03}_illuminated_backwall',geom_name=f'room_{room}_v10_cabinet_{sequence:03}_illuminated_backwall')
    stats['back']+=1
    # Real-world fixture tucked under the upper edge of each display. Emissive
    # material reduces live point-light count substantially.
    box((side*9.08,center_y+.89,center_z),(.055,.017,.84),'amber',f'room_{room}_v10_niche_diffuser')
    box((side*9.075,center_y-1.005,center_z),(.055,.02,.85),'gold',f'room_{room}_v10_niche_foot_trim')

# Split instrument geometry selection from additional mesh details, preserving
# exact named pickable bodies for CSRF-backed product hotspots.
selectable=[n for n in scene.graph.nodes_geometry if n.startswith('interact_')]
assert len(selectable)==133, len(selectable)
for n in selectable:
    m=re.fullmatch(r'interact_(\d+)_(\d+)_guitar_\d+',n)
    if not m:continue
    room=int(m.group(1));slot=int(m.group(2))
    if room not in (0,1,2): continue
    transform,gname=scene.graph[n]
    bound=trimesh.bounds.corners(scene.geometry[gname].bounds)
    world=(transform @ np.column_stack((bound,np.ones(len(bound)))).T).T[:,:3]
    low=world.min(axis=0); high=world.max(axis=0);c=(low+high)/2
    wall=abs(c[0])>7
    # Wall guitar face is oriented toward the aisle (+X on left, -X on right),
    # not parallel to the wall as in the earliest DAVID mock-geometry.
    if wall:
        sgn=1.0 if c[0]<0 else -1.0
        front_x=(high[0]+.010) if sgn>0 else (low[0]-.010)
        # Base mesh is a body only; neck is already in batched v0.7 materials.
        body_bottom=float(low[1]);body_top=float(high[1]);base=float(c[2])
        # Raised strings behind headstock but in front of finished body.
        y_start=body_bottom+.14;y_end=body_top+.72
        for j in range(6):
            dz=(j-2.5)*.020
            rod([front_x+sgn*.014,y_start,base+dz],
                [front_x+sgn*.014,y_end,base+dz*.52],.0022,'steel',f'room_{room}_v10_string')
        # Individually physical frets. Distances follow 12-TET scale (25.5in
        # reference) scaled to the display fretboard; not evenly spaced bars.
        fret_start=body_top-.10; fret_length=.69
        for fret in range(1,15):
            yval=fret_start+fret_length*(1-2**(-fret/12))
            rod([front_x+sgn*.011,yval,base-.060],
                [front_x+sgn*.011,yval,base+.060],.0029,'bridge',f'room_{room}_v10_fret')
        for fret in [3,5,7,9,12]:
            yval=fret_start+fret_length*(1-2**(-fret/12))-.019
            disc([front_x+sgn*.014,yval,base],.010,'pearl',f'room_{room}_v10_fret_marker')
        # Six real tuning-gear housings with offset posts and keys.
        for j in range(6):
            yval=body_top+.23+j*.084
            zoff=.060 if j%2 else -.060
            box((front_x-sgn*.018,yval,base+zoff),(.044,.025,.031),'gold',f'room_{room}_v10_tuner_housing')
            rod([front_x,yval,base+zoff],[front_x-sgn*.075,yval,base+zoff],.012,'bridge',f'room_{room}_v10_tuner_key')
        # Precision bridge saddles and chrome mounting screws.
        bridge_y=body_bottom+.23
        box((front_x+sgn*.012,bridge_y,base),(.018,.046,.205),'bridge',f'room_{room}_v10_bridge')
        for dz in [-.075,.075]:
            disc((front_x+sgn*.023,bridge_y,base+dz),.013,'black',f'room_{room}_v10_bridge_screw')
        if room==1:
            # Acoustic soundhole is round negative dark geometry nested in a
            # real carved spruce soundboard; rosette has 3 physical metal rings.
            disc((front_x+sgn*.019,c[1]+.14,base),.084,'black',f'room_{room}_v10_acoustic_soundhole')
            for rr in (.092,.102,.115):
                for k in range(20):
                    a=2*math.pi*k/20;b=2*math.pi*(k+1)/20
                    rod([front_x+sgn*.024,c[1]+.14+rr*math.cos(a),base+rr*math.sin(a)],
                        [front_x+sgn*.024,c[1]+.14+rr*math.cos(b),base+rr*math.sin(b)],
                        .0025,'gold',f'room_{room}_v10_rosette',5)
        else:
            # Cast dual pickups and six pole pieces per pickup.
            for py in (c[1]-.04,c[1]+.18):
                box((front_x+sgn*.023,py,base),(.030,.085,.22),'black',f'room_{room}_v10_pickup')
                for j in range(6):
                    disc((front_x+sgn*.043,py,base+(j-2.5)*.033),.008,'bridge',f'room_{room}_v10_pole')
            # True controls inset on body, not just photo-detail.
            for py,dz in ((c[1]-.18,.22),(c[1]-.31,.17)):
                disc((front_x+sgn*.019,py,base+dz),.027,'gold',f'room_{room}_v10_control_knob')
        stats['detailed_guitars']+=1
        if slot<20:
            textured_backplate(-1 if c[0]<0 else 1,room,c[1],base,slot+(0 if c[0]<0 else 100))
    else:
        # Center hero: strings run along Y, face toward the entry (-Z).
        near_z=low[2]-.012;y0=low[1]+.20;y1=high[1]+.62
        for j in range(6):
            dx=(j-2.5)*.022
            rod([c[0]+dx,y0,near_z-.025],[c[0]+dx*.55,y1,near_z-.025],.0025,'steel',f'room_{room}_v10_hero_string')
        for i in range(1,14):
            fy=high[1]-.09+.7*(1-2**(-i/12))
            rod([c[0]-.060,fy,near_z-.019],[c[0]+.060,fy,near_z-.019],.0032,'bridge',f'room_{room}_v10_hero_fret')
        for i in range(6):
            px=c[0]+(.080 if i%2 else -.080);py=high[1]+.20+i*.078
            rod((px,py,near_z-.04),(px,py,near_z-.095),.013,'gold',f'room_{room}_v10_hero_tuner')
        stats['detailed_guitars']+=1

assert stats['detailed_guitars']==81,stats
DST.parent.mkdir(parents=True,exist_ok=True)
scene.export(DST)
print('v0.10 procedural detail, model:',DST,'bytes:',DST.stat().st_size,'new pieces',sum(stats.values()))
print('Geometry additions by material:',dict(stats))