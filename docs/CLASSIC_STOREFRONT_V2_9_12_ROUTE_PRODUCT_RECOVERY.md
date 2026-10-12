# Prof Erny's Music v2.9.12 — Page Not Found / product-link recovery

**Date: 2026-10-12. The current project is a conventional navy/gold PHP/MySQL storefront, NOT the historical DAVID 3D showroom.** Work only from `classic-storefront-v1` and the verified conversation source ZIP.

## Merchant-reported regression
After extracting v2.9.11, the merchant reported "Page Not Found" across site pages and product links; product detail pages would not open. Existing-site full ZIPs intentionally EXCLUDED `.htaccess` and `app/bootstrap.php` to protect the merchant's installation. However current `app/store.php` relied on `path_url('product.php')` and `path_url('about.php')` to rewrite legacy root file names to canonical `shop/product.php` and `pages/about.php`. Old preserved bootstrap or Apache rewrites could point at nonexistent root URLs.

The correct fix is compatibility and direct PHP-file routing, **not** rerunning the fresh installer, modifying the DB, publishing hidden products or disabling safety checks.

## Implemented in local v2.9.12 release
- `app/store.php` replaces reliance on potentially old `bootstrap.php:path_url()` with `erny_public_base_prefix()` and robust `base_url()` that map legacy navigation/menu/footer/product image/cart URLs to physical `/shop/`, `/pages/`, and `/api/` PHP files. Works from root and nested subfolder installations without mod_rewrite. `shipping-returns.php` is explicitly mapped.
- 13 tiny root compatibility PHP include shims for `catalog.php`, `product.php`, `cart.php`, `checkout.php`, `order-confirmation.php`, `about.php`, `contact.php`, `rentals.php`, `repairs.php`, `school.php`, `shipping-returns.php`, `media.php`, and `installed.php`. These forward old PHP entrypoints to the exact current folder scripts and preserve POST methods without losing checkout/cart parameters. Intentionally retains protected host `.htaccess` untouched.
- `shop/product.php`: a legacy **16-character hexadecimal public original-store record ID** redirects to its proper `shop/public-product.php` *browse-only* detail, rather than being cast to numeric DB product ID and showing Product Not Found. Numeric active merchant product IDs still use normal SQL-backed detail pages and stock checks.
- `api/search.php` uses the same canonical URL resolver for suggestions and exact `/api/media.php` image endpoint; `pages/repairs.php` and `shop/checkout.php` use canonical post-action redirect paths.
- No changes to v2.9.11 category artwork, 13 parent/58 child taxonomy, product/category mapping, active/hidden/demo status, stock, prices, customer/order data, media rights, live payments, installer or recovery credentials. No 3D.

## Verification, exact scope
- **Real local PHP HTTP** with a deliberate OLD `path_url` that does NOT map root filenames and with NO Apache rewrite rules: homepage links, Shop catalog, active numeric product detail and legacy `/product.php` alias, original-store preview/detail, hex-id legacy redirect, About, Contact, Rentals, Shipping & Returns, populated subcategory, all old root aliases and canonical search-suggestion links PASS.
- Standalone simulated nested website prefix `/store/` generates the correct `/store/shop/product.php`, `/store/pages/about.php`, and media paths without relying on bootstrap mapping: PASS.
- `tests/source_http_v271.py`: 114 historical browse-only records, catalog pagination, search, category filtering, source product detail and safe 404: PASS.
- `tests/category_visibility_v298.php`: populated-only public categories, no hidden/demo publish: PASS.
- `tests/category_navigation_v297.php`: direct click, legacy category aliases, explicit staff mapping: PASS.
- `tests/smoke_release.py`: 122 PHP syntax checks, Node JS check, branded layout, protected installer and local fake-DB homepage: PASS (updated an old test fixture that omitted category-visibility modules).
- `tests/route_structure_smoke.py`: verified exactly 13 safe compatibility root scripts, full real route handlers and installation guard: PASS.
- ZIP integrity/CRC, internal manifest and hotfix/full file-by-file identity tests: PASS.

**Not verified:** Merchant's actual hosting document root, Apache configuration, PHP-FPM permissions, real MariaDB contents or any installed copy. `https://proferny.com` still appears to be the existing Squarespace site; it is not evidence of the user's deployed PHP staging environment. If a canonical `/shop/product.php?id=N` returns a branded "Instrument Not Found", staff must verify its DB status is `active`, not merely a hidden imported draft. Do not auto-enable payment or inventory.

## Downloadable artifacts (conversation ZIPs, not yet synced executable source to GitHub)
- `prof-ernys-v2.9.12-ROUTES-AND-PRODUCTS-HOTFIX.zip`: 20,783 bytes; 18 executable changed files + README. SHA-256 `7d9ca907db4704684d0240323dc19256ad1a6fb05edf2e3813dbbb9b6fd5f315`.
- `prof-ernys-v2.9.12-FULL-WEBSITE-EXISTING-INSTALL.zip`: 35,375,069 bytes; 449 deployable files + README, SHA-256 `2a3655861287fb9b6a3956deac80f41db3f6d26187c81661fbc423b9d67bc0c7`.
- `prof-ernys-v2.9.12-SOURCE-AND-TESTS.zip`: 61,101,853 bytes, SHA-256 `dd0cc3505984f0e64438d0befe5ca3abb330e79c4646f37813eb96eefce9006a`, development only, not for extraction over installed site.
- `prof-ernys-v2.9.12-RELEASE-CHECKSUMS.json` gives exact hashes of changed files and archives.

## Installation and rollback
User's hosting has previously denied PHP updater writes to `admin/categories-v292.php`. Prefer cPanel/File Manager: full independent files + SQL backups first; extract the small hotfix if already on v2.9.11 or the full safe existing-site ZIP if current files are uncertain. **Merge individual files, never delete site directories**. Packages preserve `config/`, `app/bootstrap.php`, `recovery/`, `install/`, `storage/`, `.htaccess`, `admin/upgrade-center.php`, customer records and SQL. Manual extraction is not auto-rollback; retain backups and verify direct paths after uploading. Remove ZIP from public website when complete. Do not `chmod 777` or re-run installer.

**Source-of-truth caveat:** This GitHub commit is only documentation, not the actual full PHP source or deployment ZIP; executable files are in the ChatGPT conversation artifacts. Full source synchronization to this branch remains open.