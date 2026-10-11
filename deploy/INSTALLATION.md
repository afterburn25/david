# DAVID v0.3 safe preview install (NOT a production homepage replacement)

Current packaged `david-v0.3-luxury-glb-safe-preview.zip` contains only:
- `showroom-glb.php` (PHP viewer; from repo `deploy/showroom-glb.php`)
- `assets/rooms/luxury-showroom-v03-optimized.glb` (generated from `build_gallery_v03.py` + `optimize_gallery_v03.py`)
- `UPGRADE-v03.txt`.

## On shared hosting
1. Backup the current website and database through the host panel. **Do not rerun `/install/`**.
2. Extract the preview ZIP in the existing site root beside `index.php`.
3. Open `https://YOURDOMAIN/showroom-glb.php`. The existing homepage remains unchanged.
4. Browse all five rooms; test smooth movement, clicks, inspect, catalog and cart only on mapped real database products.
5. Restore simply by removing `showroom-glb.php` and the new GLB file if errors occur. The preview does not overwrite installed config/bootstrap, DB, installer, original index or customer files.

## Development/CI testing
- `pip install trimesh numpy pillow shapely scipy`
- `python build_gallery_v03.py && python optimize_gallery_v03.py && python tests_v03.py` regenerates/checks GLB locally.
- `php -l deploy/showroom-glb.php`
- For actual staging browser evidence, install Playwright and run `DAVID_TEST_URL=https://YOURDOMAIN/showroom-glb.php node tests/browser-smoke.mjs` (produces 5 WebGL screenshots, room/input sanity checks and observational FPS).
- Current source comes from repository `main`; GitHub Action `.github/workflows/scene-tests.yml` regenerates/tests and publishes optimized GLB as an Actions artifact on applicable pushes. **Check workflow completion; no automated WebGL benchmark has been verified yet.**

## Fidelity warning
The v0.3 room geometry is genuinely 3D but NOT yet photorealistically matched to user-approved renders. Photorealism, fully accurate instruments and 60 FPS still require verification. See `docs/DESIGN_TARGET.md`, `docs/BUILD_PROGRESS.md` and issues #1/#2.
