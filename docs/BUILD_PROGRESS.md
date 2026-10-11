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
