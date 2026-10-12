# v2.9.13 — correct /prof deployment root, Used link, and read-only diagnostic

Date: 2026-10-12. **Current music storefront is traditional PHP/MySQL, NOT the discontinued DAVID 3D showroom.** Work on `classic-storefront-v1`.

## Reported problem and correction
Merchant reports that `https://demo.privoralabs.com/prof/shop/catalog.php?category=Used` is "not found" and that product category listings do not appear. Merchant clarified that the website root is **`https://demo.privoralabs.com/prof/`** (not `https://demo.privoralabs.com/`). Never debug the domain root as if it were the storefront.

External public browsing tools could not fetch the demo URL; this is a limitation of the assistant's network environment, NOT evidence that the user's host or site is absent. Actual HTTP status and PHP errors on the merchant host **remain unverified**. The source ZIP contains physical `shop/catalog.php` and `assets/data/public-catalog-v271.json` with 114 source listings, but correct source files in a local ZIP do not prove successful upload/extraction on the merchant server.

## Current v2.9.13 local source changes
- `app/store.php` hides the Used & Rare public nav/footer link unless a suitable already-active listing or original-store browse-only snapshot item is present; hidden/import drafts/demo are ignored. Source snapshot contains **zero** used/preowned/vintage records.
- `index.php` removes the dead Used category CTA when no used products are visible.
- `shop/catalog.php?category=Used` returns an honest 200 empty-state rather than an application-generated category 404; this does NOT imply the actual server can serve this physical PHP path.
- `shop/departments.php` gives a clear empty-directory message if no populated categories are visible.
- No DB schema, stock, order, payment, inventory, installer, recovery or user-uploaded image writes.

## Diagnostic (temporary; separate ZIP, never permanent)
A standalone token-protected read-only script `store-deployment-check-v2913.php` goes in the **existing /prof directory containing index.php**, accompanied by a PHP and static probe under `shop/`. The key lives only inside the diagnostic PHP and a separately downloaded PRIVATE instruction text, not in any public root README. After uploading, the merchant visits the private access URL given by the instruction file.

It reports readable/missing deployment files, whether the source listing JSON exists and its count, PHP/PDO MySQL availability, connection success/no success, counts of active/hidden/demo products and staged import candidates, visible department/subcategory counts when available, and HTTP statuses of actual `/prof` routes tested by the merchant browser. It never changes DB records, shows SQL credentials, customer records, filesystem paths or raw exceptions. **Delete the diagnostic PHP and both `shop/store-route-probe-v2913` files immediately after using them.**

Interpretation:
- `shop/catalog.php` missing on disk but PHP and static `shop/` probes return 200: incomplete ZIP extraction or file ownership problem; re-extract in **existing /prof**, never `/prof/prof`.
- File exists but probes return 404: host nginx/Apache/PHP routing or docroot/alias mismatch; provider must fix.
- Probes 200 but catalog 500/503: PHP module/dependency, installed DB configuration or fatal error; inspect PHP error log, don't rerun the installer.
- Catalog 200 but no active products and hidden import candidates exist: merchant needs authorized stock/photo/price review and publication, not a blanket "make all drafts active".
- Catalog 200 with original-site cards: 114 historical browse-only records are visible but are not confirmed inventory and cannot go to checkout.

## Verified in isolated local environment
- Real PHP 8.4 HTTP web server with document root containing a **literal /prof** directory and an intentionally old bootstrap/no rewrite rules: HTTP **200** for `/prof/index.php`, `/prof/shop/catalog.php`, `/prof/shop/catalog.php?category=Used`, `/prof/pages/about.php`, static `/prof/shop` probe, PHP probe, and token-protected diagnostic.
- Existing `tests/public_route_repair_v2912.py`, `tests/source_http_v271.py`, `tests/category_visibility_v298.php`, `tests/category_navigation_v297.php` all PASS with fake PDO; 124 PHP files syntax clean.
- Full existing-site ZIP preserves site-specific `config/`, `app/bootstrap.php`, `admin/upgrade-center.php`, `recovery/`, `install/`, `storage/`, `.htaccess`, original orders and customer data. Full ZIP contains 448 deployable application files, with `index.php` at the ZIP root and `shop/catalog.php` in `shop/`; neither the diagnostic nor the probes are included in full.
- All ZIP CRC, paths, protected exclusions and hotfix/full byte-for-byte matching validated. **No real host HTTP access or merchant MariaDB/PHP-FPM check performed.**

## Available artifacts in ChatGPT conversation, NOT fully committed GitHub application source
- `prof-ernys-v2.9.13-READ-ONLY-SERVER-CHECK.zip` — 4 entries (diagnostic, 2 probes, public readme).
- `Prof_Ernys_v2.9.13_PRIVATE_DIAGNOSTIC_INSTRUCTIONS.txt` — contains unique private diagnostic URL token; **do not commit this file or token to GitHub**.
- `prof-ernys-v2.9.13-USED-NAVIGATION-HOTFIX.zip` — 4 changed PHP files plus instructions, not a guaranteed fix for a server-level 404.
- `prof-ernys-v2.9.13-FULL-WEBSITE-EXISTING-INSTALL.zip` — safe-merge full-site PHP and assets ZIP. Prefer diagnostic before this if the host's failure mode is unknown.

## Deploy guidance
Back up website files and export existing MySQL first. Use hosting File Manager because PHP updater previously reported insufficient write permission. Extract any ZIP **inside the currently installed /prof directory (the one containing index.php)** and merge individual files, not an extra nested `prof` folder. Do not chmod 777 or rerun installer. Use the separate diagnostic to observe the actual live hosting issue, then fix hosting ownership/docroot/PHP handlers or merchant DB publication as indicated. Do not claim repaired live site without live browser confirmation.
