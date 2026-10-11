# DAVID v0.13 — mutable real product images (Oct 11 2026)

## Approved change from the user
Instruments shown in each room must represent **real products** with images that the store administrator can change at any time, not permanent generic demo instruments. Preserve true walkable 3D luxury architecture; a **product photo cutout is 2.5D**, never claim it is a 3D GLB model reconstructed from one image.

## Built and locally validated (separate staging artifact)
Artifact in the October 11 DAVID ChatGPT conversation:
- `david-v0.13-SAFE-product-photo-preview.zip` — additive PHP staging package
- `david-v0.13-source-tests.zip` — exact source, inherited v0.12 GLB, tests, image references

**Files in staging package:** `showroom-glb-v13.php`, `showroom-photo-v13.php`, `catalog-v13.php`, `admin/showroom-products-v13.php`, `assets/data/product-slots-v13.json`, `assets/js/showroom-product-photos-v13.mjs`, `assets/js/david-runtime-v13.mjs`, `assets/js/gallery-collision-v07-v09.mjs`, `assets/rooms/luxury-showroom-v12-optimized.glb`, `README-STAGING-v13.md`.

## Functional design
- Generate **133 exact 3D mesh-to-showroom-slot bindings**, preserving old g1..g10. Slots (r0_001 etc.) have bounded XYZ and mesh-name checks. If old mesh changes or no product is assigned, **no invented product info**.
- Existing `products.showroom_id` contains assigned slot; use database only for brand, model, price, stock.
- Additive table `showroom_product_images`: product_id PK/FK, mime,width,height,sha256,image_data MEDIUMBLOB,updated_at. Auto-create **only upon CSRF-authenticated admin POST**, not by GET, not by installer. No directory writes/FTP.
- Authenticated admin can upload/replace/remove JPEG, PNG, or WebP <=2 MB / 12MP and swap product assignments in one transaction. Validate file upload, Fileinfo MIME, getimagesizefromstring; no SVG/PHP uploads. Slots must exist in bundled manifest.
- Product photo endpoint serves DB byte stream with validated type, SHA256 ETag 304 and nosniff. Visible active/demo only unless admin.
- Viewer loads nearby product pictures lazily into 3D stands, masks edge-connected white studio backgrounds conservatively, preserves generic 3D instrument fallback on failure, and shows exact real product image in details. Catalog photo route shares data.
- All extra scripts are **optional**, do not replace live `index.php`, `catalog.php`, `app/bootstrap.php`, `config/`, `install/`, existing admin pages or customer data.

## Verified tests
GLB SHA and 133-slot mesh/XYZ checks; Node tests for exact binding/spoofing, white-studio alpha floodfill, photo URL checks; `php -l` across 4 routes; JavaScript syntax; isolated PHP HTTP fake persistent-DB multipart PNG upload and table creation; CSRF 419, ETag 304, product swap, forged SVG rejection and photo removal. ZIP CRC/integrity. **No real MySQL integration, WebGL browser screenshot or real hardware 60 FPS benchmark yet.**

## Unfinished
Optional **per-product 3D GLB** models for full arbitrary-angle inspection; high-fidelity furniture and photoreal baked-light reconstruction; real shared host and browser tests; media thumbnail/transcoding, database storage quotas and multi-angle images. Archive exact v0.13 source on GitHub main and verify CI before declaring reproducibility; this document is not a substitute for the code.

## Rollback
Staging upload adds only new files; remove those to withdraw the preview. First authenticated save alters the database by creating an additive table and mutating *authorized* `products.showroom_id` values. Back up database first; **never auto-drop tables or auto-undo product assignments**.
