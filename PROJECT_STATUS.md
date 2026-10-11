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


## v0.10 instrument-detail staging checkpoint — October 11, 2026
**Actual local build delivered (downloadable artifacts, NOT deployed):** `david-v0.10-real-3d-detail-SAFE-staging.zip` and `david-v0.10-complete-source-and-proof.zip`. This is a **v0.7-compatible derivative with v0.9 runtime**, NOT a replacement for an unavailable v0.8 model. The v0.8 archive is absent from the available session; preserve any user-deployed version.

Added 3D nickel strings, physically spaced frets, tuner housings and posts, bridge and pickups (or acoustic rosettes) to 81 guitar body exhibits. Added 72 REAL mesh cabinet backings with procedural warm walnut/spotlight materials; no approved reference images used as backdrops. Built 5,634 detailing pieces and batched to 276 GLB mesh nodes; preserved all 133 original selectable instrument names/positions and ten fail-closed database hotspot assignments. 848,150 triangles, 16,036,020-byte optimized GLB. No payment/inventory claims from model metadata.

**Verified:** GLB round-trip/material/UV/selection invariance tests, PHP+JS syntax, 13,650 spatial collision regression checks, fake-DB PHP HTTP/GLB header, ZIP test, VTK before/after overview and close-up rendering. **Not verified:** actual WebGL browser behavior, device 60 FPS, production MySQL/CSRF cart, matching the photorealistic reference. Visual improvement is incremental and remains far below approved images.

The complete v0.10 generator/optimizer and compiled GLB are in downloadable ZIP; **they are not yet committed to GitHub main**. Source sync of v0.6, v0.7, v0.9 staging and v0.10 remains open; existing GitHub main is at v0.5 source. See `docs/V10_STAGING.md`. Never overwrite `index.php`, config, installer, bootstrap, or database while testing.

### GitHub source sync, follow-up
Verified new commits to `main`: `build_gallery_v06.py` commit `094ff2d2d448284f6f2047b42bff47b3798bdd93`, `build_gallery_v10.py` commit `886945f5cd6c9d8b4be62093f75554fcbfc0a4e5`. Other exact v0.7/v0.10 optimizers/viewer/tests, plus compiled GLB, are **not yet synced to GitHub** as of this checkpoint; use the complete source ZIP to restore them, and verify subsequent commits. v0.10 still requires v0.7 compiled baseline, and no successful CI/WebGL check has been demonstrated.


## Oct 11 2026 — v0.11 Piano & Strings geometry milestone
**Built and tested locally; not yet accepted as photorealistic.** Derived from the v0.10 optimized GLB. New `build_gallery_v11.py` replaces 24 selected low-poly violin soundboards with spline-lofted, genuinely thick 3D PBR violin bodies and models their four strings, pegs, scrolls, bridges, f-holes and fingerboards. A curved grand piano body replaces the low-poly pick mesh, with a physically raised lid, brass rim, harp/strings, 52 separately modeled white keys and 35 black keys, legs, pedals and bench. Removed four obsolete v10 violin/piano accessory batches to avoid duplicate objects. These are real 3D meshes, not image planes.

Verified optimized asset: **280 mesh nodes, 917,738 triangles, 17,782,756 bytes**, **133 unchanged selectable mesh names**, 10 exact-sha+coordinate product hotspot bindings. `tests_v11.py` passed GLB reimport, mesh topology, alpha, inherited pick geometry, PHP/JS syntax, v0.9 movement/hotspot runtime tests and isolated fake-DB PHP HTTP 200 plus GLB header. Offscreen VTK render comparisons for piano, violin and salon were generated. **WebGL browser interactions, 60 FPS, live MySQL and photo-reference fidelity are NOT verified.** Visible result is better shaped but still stylized.

Downloadable conversation artifacts: `david-v0.11-safe-showroom-preview.zip` (6 files; excludes installer/bootstrap/config/index) and `david-v0.11-source-tests-proof.zip` (25 files including GLB and all four approved reference PNGs). Note: source and binary GLB are **not yet committed to GitHub main**; next step is to sync exact build scripts and re-run CI. Never use a staging package to overwrite the live application homepage or installer.

## v0.13 replaceable actual product images — October 11, 2026
A new **isolated staging v0.13** feature was implemented, NOT a production replacement: 133 exact mesh/XYZ positions across five 3D galleries, admin-only JPEG/PNG/WebP image uploads to new additive MySQL BLOB table without writable PHP directories/FTP, CSRF-safe product-to-position reassignment, photo endpoint with ETag, lazy product-image stands (clearly **2.5D** photo cutouts within actual 3D architecture), optional image catalog, and real product-image detail panel. Existing unassigned 3D instruments remain as fallback. Verified PHP/JS syntax and Node binding/background-removal tests plus isolated fake-persistent-DB HTTP upload/slot swap/CSRF/file validation/ETag. **No real MySQL host, actual WebGL or 60 FPS verification, no photoreal room fidelity.** Packages: `david-v0.13-SAFE-product-photo-preview.zip` and `david-v0.13-source-tests.zip` in Oct 11 conversation. The v0.13 source is **not yet fully committed**; see `docs/PRODUCT_MEDIA_V13.md`. Never deploy by overwriting installer/config/index; DB is modified only on authenticated admin save.
