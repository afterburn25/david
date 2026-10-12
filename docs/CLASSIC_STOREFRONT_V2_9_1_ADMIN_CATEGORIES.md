# Prof Erny's Music v2.9.1 — Admin import visibility, demo cleanup and exact original-shop categories

Date: October 11, 2026. **Classic PHP/MySQL store only**; the 3D showroom is obsolete for current development. This is a **locally tested staging release, not installed on the merchant's live store**.

## User-reported problems addressed
- Imported items were missing from ordinary **Admin > Products** because `catalog_import_candidates` stores pending source rows separately from the `products` inventory table. New admin UI shows both paginated stored products (published and hidden drafts) and a paginated **Pending Imported Records** queue with an authenticated, CSRF-checked **Create Hidden Draft** action. Staff must stage old-site snapshot data in Catalog Migration if there are no candidates. Never infer on-hand stock from public listing snapshots.
- Demo records (`status='demo'`) are removed from normal product/inventory views. An **opt-in manual** cleanup action after SQL backup deletes only untouched, zero-stock `DEMO-*` starter SKUs, excluding rows with linked order items, photos, wishlist, school lists, specs, adjustments or imports; operations are transactional and audited. Fresh installations no longer seed fake inventory. Existing-site patch **excludes installer**.
- Actual original-shop categories: 31 observed top-level labels, including Cajun & Louisiana Items, Guitar & Bass Strings, Effects Pedals, USED GEAR sections, School/Orchestral-related categories and Prof's Clearance Corner; 8 child labels verified from individual shop pages. Exact taxonomy JSON at `assets/data/original-shop-categories-v291.json`. Shop filters, admin editing/importing, the five approved homepage category-photo tiles and a collapsible complete homepage category directory all use this taxonomy. Raw ambiguous labels are preserved for staff classification, not guessed. The actual full Squarespace product/category/variant export is still necessary to guarantee all nested categories and assignments.
- Public snapshot catalog continues to show 114 previously indexed source listings as **browse-only**, not verified in-stock; publication still requires staff approval of exact product/variation, accurate manufacturer photo, current price and physical stock.

## Artifacts created and locally tested (conversation downloads, **not yet committed as executable source**)
- `prof-ernys-v2.9.1-ADMIN-UPDATER.zip` — 50,152 bytes, SHA256 `7d558bc7c90cc305a09e2b775f733904cf9e3b6c87b620208d474b171589c715` (12 files + SHA-pinned manifest).
- `prof-ernys-v2.9.1-CATALOG-ADMIN-HOTFIX.zip` — 49,209 bytes, SHA256 `3d5225c5220824efa47ae5d07acddaa54d166d980febd57546297805ad91f243`.
- `prof-ernys-v2.9.1-SOURCE-AND-TESTS.zip` — 4,155,341 bytes, SHA256 `f3a4c5374adf98a1e57940a463813ac04a37a41e2b9afd63cf3947cc2fae1fa7`.
- `prof-ernys-v2.9.1-CATEGORY-REFERENCE.csv` — 31 parents / 8 verified children.
- Full included documentation: `docs/UPGRADE_v2.9.1.md` in the source ZIP.

**Important source-of-truth gap:** branch `classic-storefront-v1` still contains predominantly historical DAVID 3D files and classic storefront *documentation*. The tested v2.9 and v2.9.1 PHP files, images and executable archive have not all been synchronized into GitHub. Do not claim that cloning this branch rebuilds the latest store; recover the exact v2.9.1 source archive from conversation Files Library or its downloaded copy before continuing.

## Verification and remaining work
Local checks passed: 95 PHP syntax checks, JS checks, install/homepage synthetic smoke, PHP HTTP fake-PDO admin imports and CSRF/category validation, 31 + 8 taxonomy, real localhost source storefront (homepage directory, search/filter/pagination), guarded demo deletion tests (synthetic PDO), manufacturer photo metadata tests, v2.8 publication HTTP/Chromium, and v2.0 updater parser validation of all 12 SHA-pinned file entries. **No merchant-site MariaDB/PDO integration, Apache live upgrade, live backups/recovery, payment provider or licensed image import has been verified.**

Production staging action: first back up files and SQL, use the `ADMIN-UPDATER.zip` through existing v2.0 `/admin/upgrade-center.php` (save recovery code) or manually extract the matching restricted hotfix; never use the fresh installer or full source ZIP to overwrite existing credentials, bootstrap, recovery, storage or customers. Confirm actual `catalog_import_candidates` rows/DB schema; exercise importer, draft review, image approval, categories and rollback. No automatic demo deletion or live payment enabling.

Official category references: https://proferny.com/shop , https://proferny.com/shop/guitars , https://proferny.com/shop/band .
