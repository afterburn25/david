# DAVID v0.10 staging directions
Source branch: compiled from v0.7 GLB with v0.9 runtime; not a supersession of unknown v0.8.
Download exact v0.10 complete-source/preview ZIP artifacts from October 11, 2026 conversation; current compiled GLB binary not in GitHub.
Run locally from extracted complete archive:
```sh
python build_gallery_v10.py
python optimize_gallery_v10.py
python make_v10_preview.py
python tests_v10.py
python tests/staging_http_v10.py
```
These need the previously generated v0.7 optimized GLB and dependencies included in the complete archive.
Safe-preview ZIP mounts `showroom-glb-v07-v10.php` at the existing staging PHP web root plus assets under `assets/rooms/`, `assets/js/`, and `assets/data/`.
Do not replace production index.php, config, installer, bootstrap, SQL or user files. Back up first; no database schema change.
Audit GLB and exact model coordinates before linking any price. All unmapped exhibits stay display-only. Run real WebGL and 25-view image comparison plus FPS benchmark before production approval. Actual visual fidelity still NOT MET.
