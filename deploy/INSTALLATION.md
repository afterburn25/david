# GLB preview integration — milestone 01

The first independently loadable GLB scene and optional PHP browser viewer are currently packaged as a downloadable development ZIP in the originating ChatGPT conversation. **They are not yet committed to this repository**, so retrieving this repo alone will not reproduce the scene until those files are uploaded. This distinction is intentional to avoid claiming a complete implementation.

Package contents:
- assets/rooms/luxury-five-gallery-blockout.glb (five-room 3D environment, approximate architecture)
- deploy/showroom-glb.php (optional GLTFLoader preview)
- build_rooms.py (rebuild GLB deterministically using trimesh)
- documentation.

Optional site preview: put showroom-glb.php beside the existing website index.php and put GLB at assets/rooms/luxury-five-gallery-blockout.glb. This route reads the installed PHP DB; it does not write data or override index.php. No installer, config, migrations, or schema changes.

The GLB is 1.8MB and contains 2304 scene geometry nodes. **It is not photorealistic yet**; individual 3D instruments are not accurately mapped to product IDs. No full browser screenshot benchmark has passed yet.

Next: commit source/GLB into this repo, integrate with existing PHP 3D UX, model realistic furniture/instruments and refine PBR assets, visual test against images, benchmark FPS and run shared-host compatibility checks.
