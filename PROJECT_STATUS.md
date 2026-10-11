# DAVID project status — 2026-10-11

## Actual v0.3 work performed this session
Built a new genuine five-gallery GLB from 3D meshes rather than image billboards. The modeled environments include recessed walnut instrument displays, brass trim, LED accent surfaces, textured wood/carpet/rugs, leather lounge seating, glass showcases and distinctive guitar, saxophone, violin and piano exhibits. Fixed wall instruments' edge-on orientation.

Source: `build_gallery_v03.py`, `optimize_gallery_v03.py`, `deploy/showroom-glb.php`, `tests_v03.py`, `render_gallery_proof.py`, and `assets/rooms/luxury-showroom-v03-optimized.glb`.

Result: 5,351 unoptimized geometry nodes batched to **407** nodes, preserving **322** named pickable instrument meshes. GLB size **2,947,252 bytes**. PBR material/texture maps embedded. Test: trimesh reimport, geometry and texture checks, PHP syntax, JavaScript syntax, ZIP integrity passed; five VTK offscreen room viewport renders produced.

The optional PHP viewer enables room transitions, smooth WASD+mouse/touch controls, selection/closeup, quality controls and database-backed product details for exact mapped slots only, with existing CSRF-protected cart behavior.

### NOT done / not validated
This is **not a photorealistic match** to the approved luxury images. Shapes and furniture remain too simplified and lighting needs substantial improvement. Chromium testing was blocked by sandbox network administrator on localhost; Three.js interaction, mobile behavior, FPS (60 target only), installed MySQL backend and live shared-host deployment were not tested.

### GitHub synchronization
Current v0.3 generator, viewer and GLB are packaged as `david-v0.3-full-source-and-proof.zip` in the producing conversation; **they are not committed to GitHub yet**. This must be resolved next to make repository source reproducible. The 3-file `david-v0.3-luxury-glb-safe-preview.zip` is a **separate preview route**—does not overwrite index.php, config, bootstrap, SQL or installer.

### Immediate next
Commit source and GLB to repository, enable real CI asset builds, browser capture/screenshots and FPS checks, improve high-fidelity licensed models, materials, lighting, colliders and inventory mapping. Preserve all existing database/config, never run installer on upgrade.
