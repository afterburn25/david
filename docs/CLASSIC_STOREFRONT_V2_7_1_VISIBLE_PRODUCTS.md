# Prof Erny's Music v2.7.1 — actual public listings visible on homepage (Oct 11, 2026)

## The customer problem this resolves
After v2.7 import addon, homepage still showed zero inventory because /index.php only queried MySQL products WHERE status='active', while importer staged **hidden, stock-zero drafts**. User explicitly requested **actual product listings visible on the main page**.

## Actual implementation built in the current conversation
- `assets/data/public-catalog-v271.json`: **114 distinct product listings** sampled from publicly indexed Prof Erny's original site. Known title, publicly listed price, category, source URL and previously marked sold-out flag recorded with capture date; original stock/current price not verified. Seven categories: Guitars, Band, Amplifiers, Pro Audio, Folk, Drums, Accessories.
- `app/public_catalog_v271.php`: safe, dependency-light JSON loader, stable opaque IDs, featured cross-category selection, category/brand/kind/price/search filtering, source URL allowlist, non-salable card presentation, staged-hidden-candidate conversion for admin.
- `index.php`: if no verified active products, show 10 selected real original-site listing cards in Featured Instruments instead of empty state; if live products exist, show them first then add source-preview discovery section.
- `shop/catalog.php`: combined view of published products and browsable original-site listings, 24 per source page, category/brand/type/search/price filters. In-stock-only filter excludes all unverified source previews.
- `shop/public-product.php`: dedicated safe product-preview details and inquiry actions. Original store source links. No cart/checkout for unverified preview products.
- `assets/public-catalog-v271.css`: visual styling consistent with approved navy/gold/ivory brand. Instrument images on source cards use *labeled, non-specific category artwork* while an exact rights-cleared product photograph is pending. No fake official or model-accurate manufacturer photo claims.
- `app/store.php`: links additional CSS only. `admin/catalog-import-v27.php`: one-click authorized staff action stages these 114 records as hidden import candidates in additive v2.7 MySQL tables; remains opt-in, not automatically published.  No new installer requirement.

## Downloadable verified local ZIPs in current conversation
- `prof-ernys-v2.7.1-VISIBLE-PRODUCTS-HOTFIX.zip` (45,475 bytes): incremental update for v2.0/v2.7 base, includes necessary importer and storefront files.
- `prof-ernys-v2.7.1-SAFE-UPGRADE.zip` (3,443,522 bytes), excludes installed config/bootstrap/installer/recovery/storage/migrations and .htaccess.
- `prof-ernys-v2.7.1-FRESH-INSTALL-BASED-ON-v2.0.zip` (3,497,827 bytes) for new empty database only.
- `prof-ernys-v2.7.1-SOURCE-TESTS-CATALOG.zip` (3,497,363 bytes), with scripts/tests and provenance snapshot.
- `prof-ernys-v2.7.1-SHA256-MANIFEST.json`.

These ZIPs are **created artifacts**, not committed source in GitHub. Do not claim the exact implementation is reproducible from GitHub branch until sync.

## Validations actually performed
- `tests/public_catalog_v271.php` PASS: 114 source IDs unique, 10 featured, filtering, review candidates stable, URLs allowed, no misleading stock/cart availability.
- `tests/source_http_v271.py` PASS on real local PHP HTTP with fake DB: homepage 10 original listing cards, Shop 24 per page, pagination page4, search/filter, details/invalid ID 404, no add-to-cart.
- `tests/smoke_release.py` PASS: 84 PHP syntax checks, JS syntax, synthetic HTML homepage, existing five-stage browser installer GET+CSRF and brand.
- All four packages pass ZIP integrity. Safe upgrade excludes installed credentials and installer.
- Attempted Chromium headless localhost screenshot timed out. **Do NOT report a browser visual benchmark as passed**.
- Full real MySQL import, physical stock verification, Squarespace authenticated Export All API, manufacturer/dealer licensed product photos, provider checkout, Apache shared-host tests have NOT yet passed.

## Technical honesty / merchant workflow
The user asks for actual inventory: current public catalog provides **real product identities listed by Prof Erny's online**, but public pages do NOT give authoritative warehouse/physical stock. Never call these 114 items 'in stock' or enable paid checkout until staff validates stock, prices, authorized product photos and shipping. To import ALL historic products/variants, get merchant's Squarespace Export All CSV or official API access.

## Scope safety
Continue approved conventional PHP/MySQL store, not 3D. Preserve transparent full logo, fleur-de-lis favicon, no-cropped category artwork, fancy Home/active navigation, unified search, widened persistent admin menu, branded installer, safe ZIP updater and independent rollback. Never overwrite installed config, app/bootstrap.php, install/, storage/, recovery/, customer data.

## Next
1. Sync exact new PHP/JSON/CSS/tests safely into GitHub branch without secrets.
2. Test with staging PDO_MySQL and actual PHP 8.1+ Apache/subfolder deployed site; verify source cards with existing products and aliases.
3. Obtain merchant Squarespace Export All CSV or Products API to import entire database including variants and reliable stock reconciliation.
4. License verified exact manufacturer/dealer photo assets and match by GTIN or brand+MPN; approve through existing image workflow.
5. Prevent source snapshot duplicate previews after real product approval, advance admin batch publishing UX, and monitor current inventory changes.
