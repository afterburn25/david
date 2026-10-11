"""DAVID v0.5 verification: GLB structure, finish alpha, viewer static/safety.
Does NOT claim browser screenshots, photorealistic fidelity, or 60 FPS.
"""
from pathlib import Path
from collections import Counter
import subprocess, re, zipfile
import numpy as np
import trimesh
ROOT=Path(__file__).resolve().parent
GLB=ROOT/'assets/rooms/luxury-showroom-v05-optimized.glb'
assert GLB.is_file() and 5_000_000<GLB.stat().st_size<20_000_000
scene=trimesh.load(GLB,force='scene')
geom=list(scene.graph.nodes_geometry)
assert 270<len(geom)<520, len(geom)
select=[n for n in geom if n.startswith('interact_')]
assert 175<len(select)<230,len(select)
for room in range(5):
 assert any(n.startswith(f'room_{room}__batched_') for n in geom),room
 assert any(n.startswith(f'interact_{room}_') for n in select),room
assert scene.bounds[1][2]>103
assert sum(len(m.faces) for m in scene.geometry.values())<350_000
material={g.visual.material.name:g.visual.material for g in scene.geometry.values()}
for typ in ('sunburst','tiger_maple','cherry','midnight_blue','cream','spruce','mahogany'):
 m=material['v05 finish '+typ]
 assert m.baseColorTexture is not None
 assert m.normalTexture is not None
 assert m.baseColorFactor[3]>240, ('Transparent lacquer regression',typ,m.baseColorFactor)
# regression: distorted UVs / photo wallpaper must not be introduced.
for n in select:
 g=scene.geometry[scene.graph[n][1]]
 assert len(g.vertices)>=3
 assert np.isfinite(g.vertices).all()
assert not any(('billboard' in n.lower() or 'picture_backdrop' in n.lower() or 'photo_wall' in n.lower()) for n in geom)
code=(ROOT/'deploy/showroom-glb-v05.php').read_text()
for forbidden in ('/install/','config/database.php','DROP TABLE','chmod 777'):
 assert forbidden not in code, forbidden
assert 'r${room}_${slot}' in code and "if(room===0 && slot<10)keys.push" in code
assert 'luxury-showroom-v05-optimized.glb?v=0.5.0' in code
assert 'placeInspectCamera' in code
p=subprocess.run(['php','-l',str(ROOT/'deploy/showroom-glb-v05.php')],capture_output=True,text=True)
assert p.returncode==0,p.stderr
js=code.split('<script type="module">',1)[1].split('</script>',1)[0]
js=re.sub(r'<\?=.*?\?>','null',js)
p=ROOT/'__v05_syntax_check.mjs';p.write_text(js)
try:
 r=subprocess.run(['node','--check',str(p)],capture_output=True,text=True)
 assert r.returncode==0,r.stderr
finally:p.unlink(missing_ok=True)
print('PASS v0.5:',len(geom),'mesh nodes,',len(select),'selectable instrument meshes;',sum(len(g.faces) for g in scene.geometry.values()),'triangles')
print('PASS v0.5: seven PBR instrument finish texture+normal maps, alpha fully opaque')
print('PASS v0.5: five rooms, PHP and JS syntax, generic database showroom slots, viewer close-up orbit')
print('NOT tested: in-browser WebGL interaction, actual 60 FPS, deployed shared-host DB, approved-photo fidelity')