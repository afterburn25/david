# Prof Erny's Music — Catalog Import & Authorized Product Images v2.7 (2026-10-11)

## Current scope
Continue the user-approved **normal** PHP/MySQL e-commerce storefront, not the old DAVID 3D showroom. Preserve the navy/gold/ivory site, transparent main logo, gold fleur-de-lis favicon, full uncropped category images, one seamless search bar, admin sidebar state persistence and safe installer/updater.

## Actual locally built artifacts
- `prof-ernys-v2.7-CATALOG-IMPORT-ADDON.zip` — 26,912 bytes; SHA-256 `3ed4e2fcf8062710219f5bf0467a68e0dd2faed5af97265310abf74f3e99f11a`; strictly new files, no existing PHP/config/installer overwritten.
- `prof-ernys-v2.7-FRESH-INSTALL-BASED-ON-v2.0.zip` — 3,458,479 bytes; SHA-256 `738bb762e7dbf4a09f4bf128b7be78fbcc104474db47993b86eb6cdef8eb2b7d`; source baseline explicitly v2.0.0, plus previously verified admin sidebar hotfix and new v2.7 importer. It **does not** contain all speculative/unverified v2.1–v2.6 features.
- `prof-ernys-v2.7-SOURCE-AND-TESTS.zip` — 3,480,143 bytes; SHA-256 `81a1ad56bd5b0fb08b8f018326c3a733999b76077d5b0bbaf2a012a31d2d7316`; with all source, tests and example CSVs.
- Checksums `prof-ernys-v2.7-RELEASE-CHECKSUMS.json`.

The ZIPs exist as downloaded conversation artifacts; they are **not yet GitHub binaries**. This document is a handoff; do not claim GitHub has the actual source until fetched and verified.

## What v2.7 code provides
New `admin/catalog-import-v27.php`, `app/catalog_import_v27.php`, `app/manufacturer_media_v27.php`, and CSS/JS.
- Squarespace **Export all CSV** bulk upload with variants, original SKU/GTIN/MPN/price metadata, dedupe keys, MySQL BLOB staging and automatic 175-row batches; creates only HIDDEN/stock-zero product records. Original records, prices and stock never overwritten.
- Squarespace official v2 Products API token-in-POST one-page-at-a-time, cursor pagination; token not saved.
- Public `proferny.com` catalog import fallback; cannot be assumed complete, even with public JSON format.
- 20 **sample public listings** reviewed from the indexed original site, provided in a CSV but NOT bulk-imported to production.
- Manufacturer image-source discovery per brand/product name and MPN; merchant-authorized asset feed CSV, strict exact MPN + brand or GTIN match, licensed/source review + explicit staff approval; image source via official branded product page and separately approved HTTPS asset CDN host.
- Secure cURL image retrieval (no redirects, public IPv4 validated and pinned against SSRF), raster MIME, size/dimension validation, MySQL product_images insertion only after staff approval, no existing image replacement without checkbox.
- Optional white-background flood-fill cutout with GD; source image is preserved if unsafe or GD unavailable; store product image display uses `object-fit:contain`.

## Verification
- All 81 PHP files in the assembled source lint clean; Node.js syntax check for the importer passes; archive integrity and protected-path exclusion pass.
- Pure PHP test fixture verifies CSV variants, price parsing, stable source keys, manufacturer MPN/GTIN identity, official-domain normalization, spoofed-domain rejection, private-IP rejection; tests pass.
- **NOT verified:** a live complete Squarespace export/API authorization (merchant credentials not provided), images from dealer-licensed feeds (none supplied), actual manufacturer image download/transparency on shared hosting, real MySQL staging/migration, 10k-record performance, installed site/upgrade end-to-end.
- As a result **the user's actual entire catalog has NOT been imported to the production site yet** and **no official photographs were falsely claimed to have been retrieved**. The merchant must provide a Squarespace Export all CSV or use an API token in admin and provide authorized manufacturer/dealer images or rights-cleared feed.

## Safety & deployment
- Existing v2.0+ PHP site: apply new-file-only addon in staging; visit `/admin/catalog-import-v27.php`; click Prepare import tables and then Upload Squarespace CSV. Do not rerun `/install/`. Existing `admin_ui.php`, config, bootstrap, storage, installer, recovery and checkout are never overwritten by addon.
- New empty DB only: fresh-install package includes added idempotent schema and Sidebar Memory navigation link.
- Keep all imported listings hidden and zero-stock until staff verifies exact image, manufacturer model, price, stock, rights and fulfillment.

## Next tasks
1. Obtain merchant Squarespace Export all CSV (or authorize official Products API) to populate ALL real products; inspect counts, variants and duplicate behavior.
2. Obtain official manufacturer dealer asset feed, product-accurate MPN/GTIN and commercial image reuse permissions. Fetch approved images to MySQL and review complex transparency cutouts.
3. Sync actual new source to GitHub; test with staging MariaDB+PHP extensions, batch progress for large files, and cross-session rollback; keep admin navigational hierarchy state.
4. Do not enable untested live payments or break v2.0 updater/recovery.
