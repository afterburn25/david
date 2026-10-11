# DAVID status — v0.5, 2026-10-11

**Status: genuine five-room 3D reconstruction IN DEVELOPMENT, not photorealistic and not production acceptance.**

## Verified in this milestone
- Rebuilt from existing v0.4 GLB source; adjusted 81 guitar body meshes with world-space proper UV mapping and 7 physically based material finishes (sunburst, tiger maple, cherry, midnight blue, ivory, spruce, mahogany). Seven material normal textures were included.
- Added physical instrument hardware and trim (humbuckers, volume controls, pearl fret inlays), ceiling/coffer surfaces, warm LED accents in real 3D recessed niches and cabinetry.
- Fixed an actual v0.5 regression during rendering: integer baseColorFactor alpha 1 caused the texture instruments to become nearly invisible. Changed to floating-point 1.0 and enforced opaque-alpha testing; VTK rerender confirms visible instruments.
- 5 connected galleries, **352 mesh nodes**, **195 pickable meshes**, **197,978 triangles**, **9,903,168-byte optimized GLB**.
- New `showroom-glb-v05.php` viewer with product close-up orbit and wheel zoom, stable admin product mapping `r{room}_{slot}` with `g1`-`g10` backward compatibility, versioned GLB cache key.
- GLB reimport and PBR alpha regression checks passed; PHP and JavaScript syntax checks passed; five independent VTK offscreen proof images generated. The safe preview package contains only new preview files, never installer/config/bootstrap/index.

## Current visual gap
Five rooms remain stylized/mid-detail, not photorealistic. The modeled ceilings and instrument silhouettes still visibly deviate from the approved luxury photographs. No WebGL browser screenshot comparison or 60 FPS device benchmark has passed. The GLB is slightly larger than v0.4 and still needs production-grade compression + LOD.

## Source synchronization gap
The v0.5 scripts and GLB are in the conversation's `david-v0.5-*` downloadable archives. GitHub `main` may still lack v0.4/v0.5 generator/viewer/binary assets: fetch/verify before claiming it is a fully reproducible source. Commit them through a real GitHub-capable workflow; no fake commits.

## Next iteration priorities
1. Ensure all generation scripts and GLB/CI artifact in afterburn25/david `main`.
2. Obtain high-detail licensed instrument and furniture GLBs, assemble them into actual modeled architecture; bake soft GI and realistic cabinet/ceiling lighting.
3. Use full Three.js WebGL browser screenshot and FPS benchmark; test clicks, closeup orbit, keyboard/touch, room transitions, collision, cart security and staging upgrade.
4. Replace production homepage ONLY after visual acceptance and automated safe rollback; never overwrite installed credentials or rerun installer.

## GitHub source sync completed — 2026-10-11 (v0.5)
Verified committed to main: `build_gallery_v04.py` (`c509d18`), `build_gallery_v05.py` (`bdd2bed`), `deploy/showroom-glb-v05.php` (`964c607`), `optimize_gallery_v04.py` (`80c99b0`), `optimize_gallery_v05.py` (`fccfe36`), and `tests_v05.py` (`4a78e6f`). CI rebuild workflow updated in commit `6061ba1` and targets a downloadable GLB build artifact. Previous source sync gap is now fixed for generators/optimizer/viewer/tests; compiled GLB **is not tracked in main** and a successful workflow run has **not yet been verified**. A v0.5 full source/proof ZIP and separate safe-preview ZIP were generated in the project ChatGPT conversation. Structural local tests PASS; live WebGL/FPS/fidelity still unverified.
