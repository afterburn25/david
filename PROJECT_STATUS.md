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


## Repo sync addendum — Oct 11 2026
- Committed `optimize_gallery_v03.py`, `tests_v03.py`, `docs/DESIGN_TARGET.md`, and `docs/ASSET_PROVENANCE.md` to `main`.
- The full `build_gallery_v03.py`, `deploy/showroom-glb.php`, and optimized GLB binary are **still only in the downloadable source ZIP**, not the repository. See [GitHub issue #1](https://github.com/afterburn25/david/issues/1). Do not claim the GitHub source is complete yet.
- Fidelity improvements/asset sourcing tracked at [issue #2](https://github.com/afterburn25/david/issues/2).
- The CI workflow exists but source-dependent validation cannot go green until issue #1 is resolved.


## Source sync correction — 2026-10-11
The original v0.3 `build_gallery_v03.py` Python generator and `deploy/showroom-glb.php` viewer have now been committed to `main`, alongside `optimize_gallery_v03.py` and `tests_v03.py`. GitHub Actions has a scene-generation/validation workflow. The compiled GLB binary and offscreen screenshot contact sheet are still supplied in the downloadable source ZIP, not directly committed into main. A workflow-produced binary artifact may be available after CI runs; verify the run, do not presume success. See issue #1 for closure criteria.
