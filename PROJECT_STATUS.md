# Project status — 2026-10-11
State: EARLY 3D RECONSTRUCTION, NOT PHOTOREALISTIC; latest prior PHP site build v0.5.0 is incomplete compared with approved images.

Existing: PHP/MySQL product catalog, admin, orders/requests, repairs; Three.js walkable prototype and product hotspots, simplified instruments.

Now: produce REAL 3D GLB architecture and furnishings matching approved main gallery, acoustic hall, electric vault, brass/woodwind, piano/string salon. Integrate GLBs into site without flat photo panels. Maintain optimized movement and clickable instrument product IDs.

Missing: high-fidelity GLB instrument assets, realistic PBR materials/baked GI, 5-room integrated navigation and testing, verified photo-aligned browser screenshots, measured FPS, real shared-host install tests, safe deployment checks.

Only call a milestone complete if the code/assets and verification evidence exist.


## 2026-10-11 — optimized GLB milestone
Five-room GLB was exported and geometry batching reduced the node count from 2304 to 212 while retaining clickable instrument bodies. Trimesh structural tests passed, PHP preview viewer syntax check passed; ZIP integrity passed. Binary asset/scripts are currently in ChatGPT downloadable milestone-02 package, **not yet committed to this repository**. This is an architectural 3D blockout, not the photorealistic reconstruction requested. Interactive Chrome/WebGL screenshot benchmark is still pending.
