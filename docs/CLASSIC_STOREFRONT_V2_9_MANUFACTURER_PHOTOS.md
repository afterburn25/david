# v2.9.0 Manufacturer-specific catalog images (2026-10-11)

## User directive
Replace generic category illustrations on **individual product listings** with photographs of the EXACT manufacturer product/variation. No random product photos, no mislabeled stock or counterfeit/AI imagery passed off as an actual SKU.

## Implementation completed as staging PHP code (not deployed)
- `app/public_catalog_v271.php` and `shop/public-product.php`: use the locally stored approved manufacturer photo from `api/manufacturer-image-v29.php` when an exact manufacturer image is approved. Otherwise use an explicitly labeled **Exact manufacturer product photo pending** placeholder. No generic category-image-as-SKU stand-ins. Existing **category navigation** still uses approved instrument cutouts.
- `app/source_manufacturer_media_v29.php`: additive `source_manufacturer_photos_v29` MySQL BLOB table with image bytes, SHA-256, provenance, exact manufacturer page, stated media rights, staff approver and pending/approved state. cURL fetch from public IPv4 HTTPS only with pinned DNS, no redirects, strict MIME/4MB check; conservative optional near-white background alpha removal via GD. Never modifies stock, price or the checkout; avoids replacing existing `product_images` without explicit image-manager workflows. Approved source photos copy to linked imported hidden products only when no photo exists.
- `admin/manufacturer-photos-v29.php`: authenticated + CSRF, setup for photo table, per-manufacturer batch for exact source pages, document merchant commercial-use permission, store downloaded photos as PRIVATE review first, allow staff visual confirmation of exact model/finish and explicit final approval before they become publicly served. Batch skips already approved photos. Optional manual official source URL + image CDN submission also stages privately first.
- `assets/js/manufacturer-batch-v29.js`: batch fetch over browser in small requests suitable for shared hosting, per-source progress and skip handling.
- `assets/data/manufacturer-page-sources-v29.json`: **20 exact official manufacturer PRODUCT PAGES** linked to original-source identifiers, currently Shure, ProTec, Graph Tech, JOYO, Crown, D'Addario. These are product-page references, not any image license or downloaded assets.
- `assets/public-catalog-v271.css` and `assets/manufacturer-images-v29.css`: consistent navy/gold responsive full-image styling (`object-fit: contain`) and honest photo-pending states.

## Actual image-import state (critical)
**ZERO manufacturer image binaries downloaded, bundled or installed. ZERO photos replaced on the LIVE site.** This working environment cannot fetch external manufacturer CDN binaries and has no real merchant image-media rights documentation or production MySQL access. A shared-host administrator needs to enter the actual dealer/press-image authorization, use the site-hosted secure batch photo retrieval where manufacturer servers permit, inspect actual photo/finish, and explicitly approve. Manufacturer pages may block scraping; authorized dealer art feed/API is the correct high-coverage solution. The original 114 public listings are NOT inventory quantity claims.

## Artifacts created in conversation, not yet GitHub source
- `prof-ernys-v2.9.0-MANUFACTURER-IMAGES-HOTFIX.zip`, 23,403 bytes, SHA-256 `3726932e2af36463f4bd0602df2459f235adfe1bb56733c604b4412ebf2cfc78`, exactly 11 changed files, no `index.php`, installer/config/bootstrap/storage/recovery/SQL migrations or customer records.
- `prof-ernys-v2.9.0-SOURCE-AND-TESTS.zip`, 4,137,867 bytes, SHA-256 `1149bda4b881556340b3a231be56f0d52f6b0e80b5dd9274633a33a7e880e521`, full source excluding live DB credential file.
- `prof-ernys-v2.9.0-RELEASE-MANIFEST.json`: per-file SHA-256, list of 20 verified source page matches, no product images claimed.

## Checks completed
- **93 PHP** syntax checks and JavaScript syntax passed.
- `tests/manufacturer_image_v29.php`: all 114 record identifiers retained, 20 manufacturer-page source matches, normalized exact brand/model identity, domain spoofing and private-host disallow, metadata parsing, additive table — PASS.
- `tests/source_http_v271.py`: real localhost PHP with fake PDO, 10 homepage/24 catalog source cards, search/filter/pagination/invalid product id, pending image has no unrelated category shot, no add-to-cart — PASS.
- Existing site fake-DB homepage, transparent logo, PHP installer GET/CSRF/five stages and no sensitive config overwrites — PASS.
- ZIP integrity/exclusion validation PASS.

## Still to do
1. Merchant to provide authorized source/press media rights and manufacturer-dealer asset feeds; run official photo importer on a staged PHP host with outbound internet and PDO MySQL, visually approve every exact model and finish. For 114 entries currently only 20 official manufacturer product **pages** are sourced.
2. Test real MariaDB, page metadata extraction against current manufacturer HTML, GD transparency and thumbnail serving, image rights policy. Do not assume all manufacturer sites permit auto-download or reuse.
3. Sync actual code and binaries into the GitHub `classic-storefront-v1` branch with source tests (this handoff is a document only), and then test staging account checkout and rollback.
4. Maintain approved normal non-3D store design, logo/fleur-de-lis, live search, admin navigation persistence, 5-step installer and non-destructive upgrades.

Never claim the customer can already see actual manufacturer images until image bytes have been retrieved, approved and loaded into the site.