"""DAVID v0.5 per-room PBR material batching; keeps named, raycastable instruments."""
from pathlib import Path
from collections import defaultdict
import trimesh, numpy as np
ROOT=Path(__file__).resolve().parent
src=ROOT/'assets/rooms/luxury-showroom-v05.glb'
dst=ROOT/'assets/rooms/luxury-showroom-v05-optimized.glb'
scene=trimesh.load(src,force='scene');out=trimesh.Scene();buckets=defaultdict(list)
selectable=0
for node in scene.graph.nodes_geometry:
    transform,geom=scene.graph[node]
    mesh=scene.geometry[geom].copy();mesh.apply_transform(transform)
    if node.startswith('interact_'):
        out.add_geometry(mesh,node_name=node,geom_name=node);selectable+=1;continue
    room=int(np.clip(round(mesh.bounds.mean(axis=0)[2]/23.5),0,4))
    material=mesh.visual.material
    # Material includes image maps; unique name is guaranteed in this generator.
    buckets[(room,material.name)].append(mesh)
for (room,name),meshes in sorted(buckets.items()):
    merged=trimesh.util.concatenate(meshes)
    node=f'room_{room}__batched_{name.lower().replace(" ","_")}'
    out.add_geometry(merged,node_name=node,geom_name=node)
out.export(dst)
check=trimesh.load(dst,force='scene')
names=list(check.graph.nodes_geometry)
assert len(check.geometry)<520,len(check.geometry)
assert sum(x.startswith('interact_') for x in names)==selectable
assert selectable>170
print('v0.5 optimized:',len(scene.geometry),'->',len(check.geometry),'nodes, pickable',selectable,'bytes',dst.stat().st_size,'triangles',sum(len(m.faces) for m in check.geometry.values()))