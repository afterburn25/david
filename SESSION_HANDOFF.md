# DAVID mandatory session handoff

**Start with:** afterburn25/david `main`, read README.md, PROJECT_STATUS.md, docs/BUILD_PROGRESS.md, docs/ACCEPTANCE.md, docs/DECISIONS.md and this file.

**Locked user intent:** replace the original Prof Erny's showroom with a genuine walkable 3D reconstruction of four approved photorealistic luxury-store images; five rooms total (Guitar Gallery, Acoustic Hall, Electric Vault, Brass/Woodwinds, Piano/Strings). No flat pictures posing as 3D. Current render quality is not accepted as final.

**Prior PHP website:** shared-host PHP 8.1+, MySQL/MariaDB, admin/catalog/repair/order request, no real card checkout. Earlier installer/redirect/config bugs; NEVER overwrite installed `config/database.php`, `app/bootstrap.php`, `index.php`, customer files or install/storage during test upgrades. Backup+rollback first.

**2026-10-11 v0.3 work (local artifact ZIP, NOT in GitHub source yet):**
- Built `build_gallery_v03.py` (PBR/texture real world geometry, 5 rooms), `optimize_gallery_v03.py` (5,351 -> 407 geometry nodes, retains 322 pickable instruments), `assets/rooms/luxury-showroom-v03-optimized.glb` (2,947,252 bytes).
- Built `deploy/showroom-glb.php`: optional preview route with controls, raycast and verified existing g1..g10 product mapping, CSRF/live cart only on confirmed products; no arbitrary SKUs/prices. Standalone HTML for reference test; production CDN Three.js/GLTFLoader.
- `tests_v03.py` passed GLB/PBR/name/path/PHP/JS syntax; `render_gallery_proof.py` produced five VTK offscreen screenshots. These renders confirmed room geometry but also show much more modeling and lighting work is needed.
- **Browser test BLOCKED**: localhost navigation `net::ERR_BLOCKED_BY_ADMINISTRATOR`; no 60 FPS or live MySQL claims.
- Safe preview ZIP contains only `showroom-glb.php`, `assets/rooms/luxury-showroom-v03-optimized.glb`, and instructions. Existing index stays untouched.

**Next moves:** commit actual source + GLB to GitHub (currently missing!), set CI asset build and tests, render in full Three.js browser, match approved image materials, commission/include properly licensed realistic GLB instruments/furniture, baked lighting and smooth collision/room culling. Only then make main showroom replacement, with rollback and full PHP app tests. Track commits and test evidence explicitly.
