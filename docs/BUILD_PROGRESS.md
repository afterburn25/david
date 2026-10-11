# DAVID build progress

## Oct 11 2026 — true-geometry milestone v0.3
- Created actual 3D GLB five-room interiors with recessed showcase bays, walnut/brass architecture, carpet/rug/wood material textures, glass cases, three-dimensional furnishings and instrument families.
- Corrected wall guitar orientation; room spacing at z=0/23.5/47/70.5/94.
- Batched geometry from 5,351 mesh nodes down to **407** while retaining **322** independently selectable body/horn meshes; optimized GLB 2,947,252 bytes.
- PHP optional viewer implemented with Five Rooms menu, WASD/drag/touch movement, close-up, object selection, adaptive resolution/FPS readout, exact (rather than invented) product mapping, CSRF cart POST.
- Tests passed: GLB geometry + material + names + UV validation, PHP and JS syntax, ZIP integrity, non-overwrite safety audit. Five VTK offscreen room renders created. **Real WebGL interaction test and FPS benchmark NOT performed; Chromium localhost is restricted in this environment.**
- VTK visuals confirm target gap: room interiors still too generic, product instruments and sofas simplified, lighting flat, texture fidelity far short of approved high-end photographs.
- Produced isolated safe-preview ZIP and full source/proof ZIP in conversation session. **Generated v0.3 source and binary GLB are not yet committed to GitHub.**

## Next priorities
1. Put complete build source and GLB on GitHub `main`, add CI asset generation/testing; no separate state silos.
2. Test in a real WebGL browser with camera screenshots and explicit hardware FPS readings.
3. Use detailed licensed 3D instrument and furniture assets, PBR normals/roughness and baked realistic illumination.
4. Preserve installed PHP/MySQL storefront. Upgrade only after backup/rollback and smoke-test.


## October 11, 2026 — v0.5 actual geometry/material upgrade
- Built `build_gallery_v05.py` on v0.4 with seven PBR wood/lacquer instrument finishes and normal-map textures on 81 guitar bodies, physically modeled pickup covers/knobs/fret inlays, ceiling plaster, niche lighting and brass details.
- Detected texture alpha regression in VTK offscreen render (integer 1 alpha was nearly transparent); fixed it with float 1.0 and added explicit opacity assertions to `tests_v05.py`.
- Optimized GLB: 352 mesh nodes, 195 individually selectable instrument meshes, 197,978 triangles, 9,903,168 bytes; five gallery screenshots rendered offscreen. PHP v0.5 viewer adds orbiting close-up, wheel zoom and real product slot format `r{room}_{slot}` with g1–g10 compatibility. No invented product price.
- Local GLB, PBR/alpha, PHP and JavaScript syntax tests passed. **60 FPS, WebGL browser behavior, MySQL deployment and approved-image fidelity remain untested.** Visual screenshots show meaningful but limited detail improvement; environment is not photorealistic.
- Committed generator/viewer/optimizer/tests source to GitHub; CI v0.5 GLB build workflow updated (`6061ba1`). GitHub combined statuses were empty at inspection, so do not assume CI passed. Compiled GLB binary remains in downloadable project ZIP, not main.


## v0.10 instrument-detail staging checkpoint — October 11, 2026
**Actual local build delivered (downloadable artifacts, NOT deployed):** `david-v0.10-real-3d-detail-SAFE-staging.zip` and `david-v0.10-complete-source-and-proof.zip`. This is a **v0.7-compatible derivative with v0.9 runtime**, NOT a replacement for an unavailable v0.8 model. The v0.8 archive is absent from the available session; preserve any user-deployed version.

Added 3D nickel strings, physically spaced frets, tuner housings and posts, bridge and pickups (or acoustic rosettes) to 81 guitar body exhibits. Added 72 REAL mesh cabinet backings with procedural warm walnut/spotlight materials; no approved reference images used as backdrops. Built 5,634 detailing pieces and batched to 276 GLB mesh nodes; preserved all 133 original selectable instrument names/positions and ten fail-closed database hotspot assignments. 848,150 triangles, 16,036,020-byte optimized GLB. No payment/inventory claims from model metadata.

**Verified:** GLB round-trip/material/UV/selection invariance tests, PHP+JS syntax, 13,650 spatial collision regression checks, fake-DB PHP HTTP/GLB header, ZIP test, VTK before/after overview and close-up rendering. **Not verified:** actual WebGL browser behavior, device 60 FPS, production MySQL/CSRF cart, matching the photorealistic reference. Visual improvement is incremental and remains far below approved images.

The complete v0.10 generator/optimizer and compiled GLB are in downloadable ZIP; **they are not yet committed to GitHub main**. Source sync of v0.6, v0.7, v0.9 staging and v0.10 remains open; existing GitHub main is at v0.5 source. See `docs/V10_STAGING.md`. Never overwrite `index.php`, config, installer, bootstrap, or database while testing.