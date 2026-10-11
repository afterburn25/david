# DAVID handoff — v0.5, 2026-10-11

Repo: `afterburn25/david` main. User selected four photorealistic luxury showroom reference images; requires TRUE fully walkable 3D rooms matching them, NOT image billboard walls or a stylized generic showroom. Five rooms: main luxury guitar gallery, acoustic hall, electric vault, brass/woodwind, grand piano/strings. Keep shared-host PHP/MySQL cart, product admin, installer safety and real product details.

## What is built v0.5
- `build_gallery_v05.py` BUILDS UPON `build_gallery_v04.py`, which BUILDS UPON `build_gallery_v03.py`. It adds realistic varied lacquer/wood PBR finishes to 81 actually modeled guitar bodies with proper UVs, seven normal maps, controls/inlays, lit niches, warm ceiling surfaces.
- `optimize_gallery_v05.py` batches architecture/material by room while preserving 195 pickable instrument meshes. Optimized GLB size 9,903,168 bytes, 352 nodes, 197,978 triangles.
- `make_viewer_v05.py` transforms the optional PHP viewer to load v05 GLB; close-up orbit and wheel zoom work in static code inspection only (real browser testing still required). Admin `showroom_id` mapping now accepts `r{room}_{slot}` (e.g. r3_2) with `g1..g10` fallback and no database migration.
- `tests_v05.py` validates GLB geometry, seven normal maps AND opacity to prevent v0.5 material alpha bug, PHP/JS syntax, five rooms, safe upgrade excluded paths. VTK render of each room generated; no WebGL benchmark.
- `david-v0.5-luxury-safe-preview.zip` only includes optional PHP preview route + optimized GLB and instructions. Does not override live `index.php` or config/install.
- `david-v0.5-full-source-with-proof.zip` includes generators/source and four approved image files, proof render PNGs, tests and deployment docs.

IMPORTANT: This is STILL NOT visually accepted / photorealistic; do not pretend the reference images themselves became meshes via single-image reconstruction. Those cannot expose behind-the-scene geometry; photo fidelity requires artistic modeling and detailed assets.

GitHub sync: run a repo read to verify which files exist on `main`. v0.5 source/GLB may remain in downloadable archive only; do not claim committed unless GitHub confirms.

Next: commit actual source & asset pipeline to GitHub, improve detailed realistic licensed instrument/furniture models, baked GI / soft shadow/reflection, screenshot comparisons from 5 views per room, WebGL user interaction FPS tests and safe staging smoke. Keep project progress/handoff updated every time.

## Repo sync checkpoint — v0.5
Main now includes committed v0.4 and v0.5 generators, `optimize_gallery_v04.py`/`_v05.py`, `tests_v05.py`, and `deploy/showroom-glb-v05.php`. CI definition was updated to build v0.5 in commit `6061ba1`; do not claim green without checking a workflow run. The compiled GLB remains in `david-v0.5-full-source-with-proof.zip` and `david-v0.5-luxury-safe-preview.zip` from the current ChatGPT conversation, and should be reproducible via the committed source. Create and validate GLB in a real runner before using as a production asset. Do not overwrite live PHP `index.php` or database config.


## Latest v0.10 staging work — continue from here
The user asked to keep going toward photorealistic WALKABLE five-room GLB showroom matching four approved images; still NOT MET.

Latest session built v0.10 *on v0.7*, not on unavailable v0.8. The full source, optimized 16,036,020-byte GLB, PHP optional route, fail-closed manifest, tests, and proof PNGs are in the **conversation downloadable `david-v0.10-complete-source-and-proof.zip`**. Safe deployment ZIP is `david-v0.10-real-3d-detail-SAFE-staging.zip`. Neither is a drop-in upgrade to live index.php.

Actual work: 81 guitar bodies with 6 strings, equal-temperament frets, real tuner geometry, pickups/bridge or acoustic rosette, 72 physically modeled textured cabinet backings. 5,634 generated details batched to 276 GLB nodes; 133 named selectable bodies unchanged. Tests PASS (geometry/PBR/opacity/UV, PHP/JS syntax, Node collision 13,650 points, fake PHP staging HTTP 200/GLB header, ZIP). VTK close-up and overview comparisons produced, visually still stylized; WebGL/FPS/live MySQL unverified.

**Missing upstream:** GitHub still missing v0.6/v0.7/v0.9/v0.10 source and compiled assets (v0.5 source exists); obtain source from downloaded full ZIP and reconcile actual deployed v0.8 before integrating. Do not claim GitHub has these files until independently fetched. When upgrading geometry, re-audit collider/mesh centers and re-author hotspot SHA manifest. Priority: proven licensed detailed 3D models, baked GI, true Chrome Three.js 25-angle screenshots and measured frame times on compatible hardware, non-destructive PHP test/rollback. Keep all project documents current.


### GitHub source sync, follow-up
Verified new commits to `main`: `build_gallery_v06.py` commit `094ff2d2d448284f6f2047b42bff47b3798bdd93`, `build_gallery_v10.py` commit `886945f5cd6c9d8b4be62093f75554fcbfc0a4e5`. Other exact v0.7/v0.10 optimizers/viewer/tests, plus compiled GLB, are **not yet synced to GitHub** as of this checkpoint; use the complete source ZIP to restore them, and verify subsequent commits. v0.10 still requires v0.7 compiled baseline, and no successful CI/WebGL check has been demonstrated.


## Oct 11 2026 — v0.11 Piano & Strings geometry milestone
**Built and tested locally; not yet accepted as photorealistic.** Derived from the v0.10 optimized GLB. New `build_gallery_v11.py` replaces 24 selected low-poly violin soundboards with spline-lofted, genuinely thick 3D PBR violin bodies and models their four strings, pegs, scrolls, bridges, f-holes and fingerboards. A curved grand piano body replaces the low-poly pick mesh, with a physically raised lid, brass rim, harp/strings, 52 separately modeled white keys and 35 black keys, legs, pedals and bench. Removed four obsolete v10 violin/piano accessory batches to avoid duplicate objects. These are real 3D meshes, not image planes.

Verified optimized asset: **280 mesh nodes, 917,738 triangles, 17,782,756 bytes**, **133 unchanged selectable mesh names**, 10 exact-sha+coordinate product hotspot bindings. `tests_v11.py` passed GLB reimport, mesh topology, alpha, inherited pick geometry, PHP/JS syntax, v0.9 movement/hotspot runtime tests and isolated fake-DB PHP HTTP 200 plus GLB header. Offscreen VTK render comparisons for piano, violin and salon were generated. **WebGL browser interactions, 60 FPS, live MySQL and photo-reference fidelity are NOT verified.** Visible result is better shaped but still stylized.

Downloadable conversation artifacts: `david-v0.11-safe-showroom-preview.zip` (6 files; excludes installer/bootstrap/config/index) and `david-v0.11-source-tests-proof.zip` (25 files including GLB and all four approved reference PNGs). Note: source and binary GLB are **not yet committed to GitHub main**; next step is to sync exact build scripts and re-run CI. Never use a staging package to overwrite the live application homepage or installer.
