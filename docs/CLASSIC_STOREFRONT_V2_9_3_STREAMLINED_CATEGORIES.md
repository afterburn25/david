# Prof Erny's Music — streamlined department taxonomy v2.9.3
Date: October 11, 2026. **Current storefront direction: conventional navy/gold/ivory PHP/MySQL shop, NOT 3D DAVID.**

## User request
The first v2.9.2 category hierarchy had 13 main departments and 103 subcategory image tiles, too many for clear browsing. Consolidate overlaps without losing old product-category associations, and make the ZIP updater no longer require manually pasting external SHA-256.

## Completed in LOCAL v2.9.3 staging archive
- Kept all 13 parent departments; consolidated **103 old subcategories into 58 displayed category tiles** (45 retired). Every department now has 2–8 subcategories.
- Preserved **all 103 old subcategory slugs/labels**, with 45 former URL slugs redirecting to a surviving category and canonicalized in old product DB assignments. Legacy source labels continue mapping; ambiguous labels (notably "Cleaning & Care" under Band vs general Accessories, and broad "Accessories") are left for merchant review instead of silently guessed.
- Retained previous image assets: **71 referenced transparent RGBA WebP image files** (13 parent + 58 child). Built mobile responsive luxury department/subcategory cards, category hero sections, edit/reorder/hide/category-photo management, and source-to-department admin mapping. Transparent merchandising art is not proof of a real manufacturer SKU photograph; some assets still need editorial acceptance.
- Admin upgrade screen no longer requires *typed external SHA-256*. The official ZIP's **per-file SHA-256 manifest, safe-path controls, PHP syntax, private file/SQL backups, admin password, recovery code, and rollback** remain enforced. Includes a ONE-TIME-QUICK-UPGRADER ZIP to manually replace the previous updater PHP on hosting accounts still enforcing a pasted SHA. Do not disable integrity checks.
- No modifications to customer/order data, stock, active product status, payment processing or installer. Staging, **not production-deployed**.

## Packaged and verified in the user's ChatGPT conversation, NOT FULLY GITHUB-SYNCED as executable source
- `prof-ernys-v2.9.3-ADMIN-UPDATER.zip` (12,297,679 bytes, SHA256 `c87f67f9ef9dfba5af0b84deb57413712d79c669958b8868672e16a5df594902`), **85 SHA-pinned files including 71 PNG/WebP-like transparent WebP images**.
- `prof-ernys-v2.9.3-ONE-TIME-QUICK-UPGRADER.zip` (4,111 bytes).
- `prof-ernys-v2.9.3-SAFE-MANUAL-UPGRADE.zip` (12,294,252 bytes).
- `prof-ernys-v2.9.3-SOURCE-AND-TESTS.zip` (26,173,215 bytes).
- `prof-ernys-v2.9.3-CATEGORY-TREE.csv` (58 rows) documents each surviving node, previous merged names and art path.
- In that source archive, consult `assets/data/departments-v292.json`, `app/categories_v292.php`, `app/category_cards_v292.php`, `shop/departments.php`, `shop/department.php`, `shop/catalog.php`, `admin/categories-v292.php`, `admin/upgrade-center.php`, `assets/departments-v292.css`, and `docs/UPGRADE_v2.9.3.md`.
- **Do not claim executable PHP/graphics are on this GitHub branch** just because this is committed; they are stored in conversation downloadable archives and require a separate verified source sync.

## Verification
- 103 PHP scripts syntax lint, JS checks, synthetic homepage/admin import test, 13 PHP active-navigation cases, real local PHP HTTP shop/catalog source-card and category-route tests with fake PDO, old slug redirects, no checkout for pending imported products.
- `tests/taxonomy_merge_v293.php`: 13 departments/58 live nodes, all 103 original identities preserved, no resurrected seeded old DB categories, custom staff names preserved, 45 redirects and old product mappings, generic ambiguous category manual review — PASS.
- `tests/taxonomy_media_v293.py`: all 71 referenced photos/illustrations RGBA transparent, image size/path — PASS.
- Chromium offline visual cards at 1440 and 390px: 13 department cards, no broken images or horizontal overflow — PASS. **Not a live website screenshot.**
- Admin updater ZIP genuine manifest/size/files/internal SHA validation against v2.0 recovery engine — PASS, 85 files, migrations=[].
- **Not yet tested:** live merchant PDO MySQL, production Apache/hosting upgrade and rollback, merchant-licensed exact manufacturer product photography, gateway checkout/payment/refunds, complete Squarespace exports, actual stock.

## Deployment guardrails / next steps
Back up both real SQL and files before any install. If installed admin upgrade screen still requires typed SHA, first apply one-time simple File Manager hotfix to `admin/upgrade-center.php`, then in admin upload manifest-based v2.9.3 ADMIN-UPDATER without an external SHA; save recovery code before final apply. Keep install/, config/, recovery/, storage/, app/bootstrap.php, system/installed.php and customer/order records untouched. Real SQL backup can only be restored by reviewed admin intervention, not automatic destructive rewind.
