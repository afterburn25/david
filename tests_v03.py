"""Structure and safe-upgrade tests. Does not assert browser FPS or deployment success."""
from pathlib import Path
from collections import Counter
import subprocess,re,zipfile,tempfile
import trimesh
R=Path(__file__).resolve().parent
A=R/'assets/rooms/luxury-showroom-v03-optimized.glb'
s=trimesh.load(A,force='scene');names=list(s.graph.nodes_geometry)
assert 100<len(names)<450,len(names)
assert len([x for x in names if x.startswith('interact_')])>=300
assert s.bounds[1,2]>100
for idx in range(5):
 assert any(x.startswith(f'interact_{idx}_') for x in names),idx
 assert any(x.startswith(f'room_{idx}__batched_') for x in names),idx
mats=Counter(m.visual.material.name for m in s.geometry.values())
for mat in ('Generated carpet PBR texture','Generated wood PBR texture','Generated rug PBR texture','American walnut satin','Brushed architectural brass','Showcase glass'):
 assert mat in mats,mat
for m in s.geometry.values():
 if m.visual.material.name.startswith('Generated '):
  assert m.visual.uv is not None and len(m.visual.uv)==len(m.vertices)
assert not any('billboard' in n.lower() or 'photo_panel' in n.lower() for n in names)
php=R/'deploy/showroom-glb.php'
assert subprocess.run(['php','-l',str(php)],capture_output=True,check=True).returncode==0
p=php.read_text();assert "require_install()" in p and 'cart.php' in p and 'luxury-showroom-v03-optimized.glb' in p
assert '<?=json_encode($catalog' in p and '<?=json_encode($csrf' in p
module=p.split('<script type="module">',1)[1].split('</script>',1)[0]
module=module.replace('<?=json_encode($catalog,JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT)?>','[]').replace('<?=json_encode($csrf,JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT)?>','""')
with tempfile.TemporaryDirectory() as temp:
 testjs=Path(temp)/'viewer.mjs';testjs.write_text(module)
 assert subprocess.run(['node','--check',str(testjs)],capture_output=True,check=True).returncode==0
print('PASS: GLB: 5 rooms, distinct exhibit picks, PBR mats, textures, non-billboard geometry, PHP+JS syntax')
print('MESHS',len(names),'PICKABLE',len([x for x in names if x.startswith('interact_')]),'BYTES',A.stat().st_size)
