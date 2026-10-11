"""Material-preserving mesh batching, with world-space per-room visibility and unbatched pickable instruments."""
from collections import defaultdict, Counter
from pathlib import Path
import numpy as np
import trimesh
ROOT=Path(__file__).resolve().parent
src=ROOT/'assets/rooms/luxury-showroom-v03.glb'
dst=ROOT/'assets/rooms/luxury-showroom-v03-optimized.glb'
s=trimesh.load(src, force='scene'); out=trimesh.Scene();groups=defaultdict(list); selectables=0
for node in s.graph.nodes_geometry:
 matrix,g=s.graph[node]
 m=s.geometry[g].copy();m.apply_transform(matrix)
 # each selectable solid retains original name so JS can raycast to actual 3D silhouette
 if node.startswith('interact_'):
  out.add_geometry(m,node_name=node,geom_name=node);selectables+=1;continue
 center=m.bounds.mean(axis=0)
 room=int(np.clip(round(center[2]/23.5),0,4))
 mat=m.visual.material
 # material object name suffices because all meshes are from exact same material library
 groups[(room,mat.name)].append(m)
for (room,material),meshes in sorted(groups.items()):
 merged=trimesh.util.concatenate(meshes)
 node=f'room_{room}__batched_{material.lower().replace(" ","_")}'
 out.add_geometry(merged,geom_name=node,node_name=node)
out.export(dst)
check=trimesh.load(dst,force='scene')
node_names=list(check.graph.nodes_geometry)
assert selectables>60,selectables
assert sum(n.startswith('interact_') for n in node_names)==selectables
assert len(check.geometry)<500,len(check.geometry)
assert check.bounds[1,2]>100
assert any('generated_wood' in n for n in node_names)
print(f'optimized {len(s.geometry)} to {len(check.geometry)} nodes, {selectables} pickable, {dst.stat().st_size} bytes')
print('PBR MATERIALS', Counter(g.visual.material.name for g in check.geometry.values()).most_common(18))
