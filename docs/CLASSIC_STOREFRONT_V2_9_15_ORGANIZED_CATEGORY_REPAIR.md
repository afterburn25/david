# Prof Erny's Music v2.9.15 — organized root, category visibility and image deployment repair

Date: 2026-10-12. Approved project remains the conventional PHP/MySQL music shop, **not 3D**. Branch: `classic-storefront-v1`. Test URL prefix: `https://demo.privoralabs.com/prof/`.

## Confirmed requirements
- **Only index.php is a PHP file in the website root**; public commerce goes in `shop/`, content in `pages/`, API in `api/`, customer pages in `customer/`, administrative code in `admin/`, support modules in `app/`, assets in `assets/`.
- Public category pages only show departments/subcategories with verified active inventory or historical browse-only source records; never count demo/hidden drafts as products. **Admin must list ALL 13 main / 58 child categories**, even staff-hidden or empty.
- Every one of the 71 taxonomy image paths must be included, reachable under **/prof/assets/**, with functional fallback image URLs even when category photo overrides fail. Do not introduce 3D assets.
- Do not overwrite installed database credentials, app/bootstrap.php, installer, .htaccess, recovery, customer records, private storage or orders.

## Specific changes in v2.9.15 locally tested source
1. Existing v2.9.12/14 root compatibility PHP shims are **NOT included in either deployment ZIP**. Full ZIP root has only `index.php` and `favicon.ico`; targeted repair ZIP root contains only `index.php`.
2. `admin/clean-root.php` is an authenticated, CSRF-gated, explicit-confirmation utility that checks byte-for-byte signatures of 12 old compatibility shims before allowing their deletion. It verifies each organized replacement exists; customized/unknown root PHP is never touched. **A merge/extract ZIP does not automatically remove older files from an installed host**; review and run cleanup only after verifying canonical pages, or remove verified copies with hosting File Manager if PHP cannot write.
3. `app/category_visibility_v298.php`: active inventory counts use only the legacy base `products(id,name,category,status)` fields if optional v292 mapping SQL fails; an incompatible optional mapping table cannot silently empty the entire public category directory. Real active product records take precedence; hidden/demo remain excluded.
4. `app/categories_v292.php` and `admin/categories-v292.php`: administrative department tree and pickers include staff-hidden and empty categories for review, while public components keep their distinct populated-only filter. Missing/outdated image_data columns fall back to built-in images without changing the merchant's database rows.
5. `app/categories_v292.php` returns application-root-aware (`/prof/assets/...`) validated, versioned image paths. `assets/js/category-fallback-v2915.js` reads PHP-provided `data-fallback-url` rather than incorrectly hardcoding `/assets/` at the domain root. A generic local fallback WebP is bundled.
6. `admin/category-health-v2915.php` is a read-only, authenticated health view with exact source/active/hidden/demo counts, configured/visible parent+child counts, missing built-in art, and custom upload counts; linked from Admin sidebar.
7. `app/store.php` uses canonical PHP routes under `shop/` and `pages/` compatible with installed older protected bootstrap/.htaccess files. v2.9.14 homepage/Shop defensive exception handling and browse-only limited-mode fallback are preserved.

## Exact artifacts generated and verified (ChatGPT conversation, NOT yet live deployed)
- `prof-ernys-v2.9.15-ORGANIZED-CATEGORIES-IMAGE-REPAIR.zip` — 96 deployable files, **7,208,267 bytes**, SHA256 `da49df71f7989d086b05a88dd00d9ccf4fb6c12228fc1e9757b2118006498fc5`. Includes all 71 referenced image WebPs and synchronized PHP/JS/CSS/JSON.
- `prof-ernys-v2.9.15-FULL-WEBSITE-EXISTING-INSTALL.zip` — 439 deployable files, **35,389,951 bytes**, SHA256 `52fb174ee09dab568710ba1b9249b32b3c3ecde390bee97b772a12ace85a8562`. Full existing-site safe merge and no root PHP shims.
- `prof-ernys-v2.9.15-SOURCE-AND-TESTS.zip` — 446 developer files, 35,403,733 bytes, SHA256 `0a9ee91fe18580811fb0c819bd651733affba2f555ca538312cb5c14e729ea3a`. Not for live extraction.
- `Prof_Ernys_v2915_INSTALLATION.txt` — manual cPanel/File Manager safe deployment instructions, including deliberate root-shim cleanup.
- `prof-ernys-v2.9.15-RELEASE-CHECKSUMS.json` — exact archive checksums.

## Local validation completed
- 87 deployable PHP files lint cleanly with PHP 8.4; 6 JavaScript files pass Node syntax checks.
- Synthetic PDO regression: all 13/58 categories stay in Admin, hidden parent stays hidden publicly, live active products survive optional mapping-table failure, legacy schema category override is preserved, images use /prof prefix, only index.php is root PHP: **PASS**.
- Real local PHP HTTP under literal **/prof/** with intentionally outdated bootstrap and no rewrite rules: homepage complete, Shop, Used bookmarked URL, department/subcategory pages, Pages, admin categories & health, **all 71 WebP asset URLs return 200**: **PASS**.
- The same HTTP tests pass both for **clean extraction of the FULL ZIP** and for **the repair ZIP merged over actual prior v2.9.14 package**, using isolated fake DB and test bootstrap.
- Actual rendered PHP category-card HTML with real images embedded into **offline Chromium** passes at 1440px and 390px: images decode, `object-fit:contain`, and no horizontal scroll. Live browser navigation to localhost is administratively blocked in this sandbox; therefore call this an offline rendering test, not live WebGL/browser production certification.
- Six v2.9.14 emergency recovery scenarios (corrupted/missing taxonomy, missing PHP category renderer, injected category or SQL exceptions), and previous public-source HTTP fixtures: **PASS**.
- Both deployment ZIPs passed CRC, duplicate-entry, traversal, 3D-exclusion, protected-path checks and exact byte-for-byte overlap. They include no legacy root PHP shims or database/config backup files.
- **Still NOT verified:** actual merchant hosting files, PHP-FPM user permissions, Apache/nginx configuration, real MySQL schema/contents, CDN cache, customer payment workflow. Browsing `https://demo.privoralabs.com/prof/` from this environment fails DNS/access. Do NOT claim deployment or live HTTP 500 resolution without actual host error logs.

## Deployment and next debugging steps
1. Download full independent site file backup and SQL backup. Hosting File Manager extraction of **focused repair ZIP** into the **existing /prof directory containing index.php** is appropriate because the user's PHP ZIP updater lacks parent-directory write permission; choose full existing-site ZIP only if code files are incomplete/inconsistent. Merge, do not replace folder trees. **No /prof/prof nesting.**
2. Visit `/prof/shop/catalog.php`, `/prof/shop/departments.php`, `/prof/admin/categories-v292.php` and `/prof/admin/category-health-v2915.php` after login. Check missing art and active/hidden/demo counts; act on the reported root cause rather than enabling hidden inventory.
3. After routes work, use `/prof/admin/clean-root.php` to remove **verified only** old v2.9.12/14 root shim files, with backup and explicit confirmation. PHP ownership restrictions may require File Manager instead. Never indiscriminately delete unknown code.
4. If the real host still throws HTTP 500, collect the **server PHP error log** for `ERNY_HOME_CATEGORY_EXCEPTION`, `ERNY_SHOP_CATALOG_EXCEPTION`, or `ERNY_PUBLIC_CATEGORY_COUNT`, redact credentials and private paths, then debug the exact exception/line. A fallback page is not proof the underlying problem is repaired.
5. Full source synchronization of the executable PHP and WebP files to GitHub remains open. This document is a handoff, not the source code itself.
