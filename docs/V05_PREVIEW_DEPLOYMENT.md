# DAVID v0.5 optional luxury GLB preview — safe shared-host deployment

## What changes
- Independent `showroom-glb-v05.php` preview page; no overwrite of `index.php`.
- `assets/rooms/luxury-showroom-v05-optimized.glb` — actual 3D room geometry with PBR instrument finishes, normal maps, ceilings, additional illuminated niches, instrument controls.
- No database migration. No install files. No changes to `config/`, `app/bootstrap.php`, `admin/`, `storage/` or existing showroom.
- PHP viewer reads the existing product catalog and maps the old `g1`–`g10` slots plus new `r{room}_{slot}` IDs without inventing prices/availability. The admin's showroom ID field can accept these short IDs.

## Test without disrupting the live storefront
1. Back up your site and database. Create a staging directory or use the current installed site root with a DIFFERENT preview filename.
2. Extract the ZIP, placing `showroom-glb-v05.php` beside the installed `index.php` and GLB under `assets/rooms/`.
3. Open `https://yourdomain.example/showroom-glb-v05.php`. The page needs HTTPS and access to cdn.jsdelivr.net for Three.js modules.
4. Use WASD/drag/touch to navigate, inspect wall instruments, click `Inspect up close`, drag to orbit, and return to the gallery. Use the FPS monitor and Auto/Performance quality settings.
5. For live product slots, edit the catalog `showroom_id` (unique VARCHAR(24)) to e.g. `r3_2` for the Brass & Woodwind room, slot 2. Unassigned displays remain `DISPLAY ONLY`; demo records cannot be purchased.
6. To roll back, remove only `showroom-glb-v05.php` and the v05 GLB. The existing homepage and database remain unchanged.

## Limitations
- This is still not photorealistic and does not yet match the approved renders at the fidelity requested. It is an iteration on real geometry and materials.
- The v0.5 GLB is approximately 9.9 MB; shared hosting should be configured to serve `.glb` with `model/gltf-binary` or `application/octet-stream`.
- No live browser WebGL interaction, actual 60 FPS measurement or MySQL connected deployment is established in this build.
- `showroom-glb-v05.php` requires the existing installed PHP application; it is not a standalone static HTML preview.

## Next: precision/high-fidelity 3D assets and proper browser QA
Model furniture & instruments with optimized detailed licensed meshes (Blender/GLB), add PBR normal/roughness plus baked GI and shadow data, validate matched cameras and mobile/desktop, then plan a tested and reversible homepage integration.