# Prof Erny's Music — v2.9.14 emergency PHP category/catalog HTTP 500 recovery

Date: October 12, 2026. **Approved project: conventional PHP/MySQL navy-and-gold music store, NOT historical 3D DAVID.** Active branch: `classic-storefront-v1`. Installed staging website: **https://demo.privoralabs.com/prof/**.

## User's actual error
The merchant reports the homepage renders until **"Shop by Department"** and stops, while pages under `/prof/shop/` return **HTTP ERROR 500**. Older diagnostic links may also display "File Not Found." External browsing and container DNS could NOT reach the merchant's staging host. Therefore the actual server-side PHP error/stack remains **unverified**; do NOT claim the site has been fixed in production. A local ZIP's successful structural tests do not prove host installation.

The timing and shared code path indicate the PHP category stack (`app/category_cards_v292.php`, `app/category_visibility_v298.php`, `app/categories_v292.php` and `assets/data/departments-v292.json`) is a strong candidate. Mixed/partially installed releases, custom category SQL data or PHP runtime exceptions can cause this symptom.

## Implemented locally in v2.9.14
1. `app/store.php`: `category_tiles()` catches any category-rendering `Throwable`, writes a private `ERNY_HOME_CATEGORY_EXCEPTION` error-log marker, and displays a small Shop listing fallback instead of truncating the homepage.
2. `app/categories_v292.php`: detects missing/stale/invalid taxonomy JSON. Restores the complete, verified v2.9.13 13-department/58-child taxonomy from read-only `app/category-defaults-v2914.php`; preserves custom DB category overrides if valid.
3. `shop/catalog.php`: buffers output inside `try/catch(Throwable)`, logs `ERNY_SHOP_CATALOG_EXCEPTION` with exception class/message and filename/line, and returns a clearly marked **limited browse-only original-store listing** rather than HTTP 500 if category/SQL code crashes. This fallback uses only `assets/data/public-catalog-v271.json` (114 indexed historical records); it does NOT claim current stock, enable checkout or publish imported drafts. It handles `/prof/shop/catalog.php` including `?category=Used`.
4. `shop/departments.php` and `shop/department.php`: recover from category exceptions to a usable Shop link/redirect, log markers, preserve non-3D design and canonical product routing.
5. The **small emergency ZIP** synchronizes 18 related runtime files (all required category PHP dependencies, original catalog data, taxonomy JSON, shop listing/detail routes); it excludes private credentials, installer, recovery, backups, customer and SQL files.

## Real local HTTP verification under literal /prof
Using PHP 8.4 built-in HTTP server, fake isolated PDO and **no Apache rewrite rules**, run `tests/recovery_http_v2914.py` with SIX scenarios:
- Full, normal category stack: PASS.
- Corrupted `assets/data/departments-v292.json` with verified backup: homepage and Shop show normal categories: PASS.
- Corrupted JSON with backup file missing: homepage completes; Shop uses browse-only fallback; logs error privately: PASS.
- Missing `app/category_cards_v292.php`: homepage completes; Shop uses fallback and logs issue: PASS.
- Injected exception in category-count PHP: homepage completes; Shop uses fallback: PASS.
- Injected PDO schema/query exception: homepage completes; Shop uses fallback: PASS.

All source HTTP regression tests PASS (114 historical source records, 24/page, browse-only links, no cart). PHP lint PASS for modified files and other app/shop PHP; package ZIP CRC, duplicate names, forbidden protected path checks PASS.

## Downloadable artifacts
- `prof-ernys-v2.9.14-HOMEPAGE-SHOP-500-REPAIR.zip` — **70,197 bytes**, 18 runtime files + instructions. SHA256 `3ca8f42b789af3c92ec76fe170682d294de724b47e9bfd0ff4878aa1e0bb126a`.
- `prof-ernys-v2.9.14-FULL-WEBSITE-EXISTING-INSTALL.zip` — **35,390,307 bytes**, 450 safe-merge deployment files + readme, SHA256 `494b889084e0d11bbf18731f08a79a7ca8d68e0542f26bc74d758d3eb6e46d9d`.
- `prof-ernys-v2.9.14-REPAIR-SOURCE-AND-TESTS.zip` — **75,227 bytes**, 18 core files and two reproduction tests, SHA256 `fe03e9705520b3cc1ad98122cdce42125c22061c4f4c5b0a1c155a071eab5043`.
- `prof-ernys-v2.9.14-RELEASE-CHECKSUMS.json` has file list and digest.

Files are generated ChatGPT conversation downloads, **not fully GitHub-sync'd executable source**. This GitHub document is NOT proof the actual site files have been deployed or that the root cause of the live 500 was verified.

## Safe deployment and next diagnostic
1. Back up the **existing** `/prof` website files and export MySQL. Host File Manager, not admin ZIP installer, because PHP update permissions previously failed.
2. Extract only the small emergency ZIP into the already-installed site folder containing `index.php` (no nested `/prof/prof/`); merge folders/overwrite included individual files. Do not delete directory trees, change `config/`, `app/bootstrap.php`, `recovery/`, `install/`, `storage/`, `.htaccess` or SQL. Never chmod 777.
3. Test exact `https://demo.privoralabs.com/prof/`, `https://demo.privoralabs.com/prof/shop/catalog.php`, `https://demo.privoralabs.com/prof/shop/catalog.php?category=Used`, `https://demo.privoralabs.com/prof/shop/departments.php`.
4. If Shop renders **"Limited catalog view"**, the visible HTTP 500 is contained but the underlying server issue remains. Retrieve the server PHP error log entry prefixed **`ERNY_SHOP_CATALOG_EXCEPTION`**, redact full private filesystem paths/credentials before sharing, and correct the actual SQL/hosting problem rather than accepting limited mode as full commerce certification.
5. If HTTP 500 persists unchanged, confirm the new `shop/catalog.php` contains `ERNY_SHOP_CATALOG_EXCEPTION`; if not, the file has NOT been replaced at the live document root (check ownership/File Manager extraction/OPcache). The actual host PHP version, module availability, MariaDB and file permissions need investigation by the hosting operator.

No 3D code or assets were introduced. Do not enable payments on unreviewed source products.