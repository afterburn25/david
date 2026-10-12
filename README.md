# Prof Erny's Music — Classic Full-Stack PHP Storefront

**Current approved work:** traditional conversion-focused online store on PHP 8.1+/MySQL shared hosting. The DAVID 3D showroom remains a separate historical experiment on main; it is not the current website design.

## Locked brand
- User-approved transparent Prof Erny's navy/gold logo.
- Gold fleur-de-lis favicon on navy.
- Navy, gold, and ivory e-commerce site with Home/Shop/Used & Rare/School Band/Rentals/Repairs/Our Story/Contact active/hover navigation.
- Unified header search, transparent photoreal instrument cutouts with object-fit: contain.
- Professional five-step branded in-browser installer.

## Current release candidate
**v1.8.0** bundles staged v1.3–v1.8 features. Read [release handoff](docs/CLASSIC_STOREFRONT_V1_8_RELEASE.md) and the [organized folder layout](docs/CLASSIC_STOREFRONT_V1_1_STRUCTURE.md).

The built v1.8.0 source and ZIPs exist as downloadable artifacts in the originating ChatGPT conversation, **not yet fully in this GitHub branch**. Do not pretend GitHub hosts the code until it has been synchronized, tested, and verified. The latest actual implementation is a PHP release candidate, not live-commerce certified.

## Shared-hosting requirements and safety
- PHP 8.1+, PDO_MySQL, Apache with .htaccess, HTTPS, MySQL/MariaDB.
- Installed site upgrades **never** overwrite app/bootstrap.php, config/, storage/, install/ or database tables.
- Use safe ZIP with full backups, run authenticated additive /admin/updates.php migrations. Never run the fresh installer on an existing store.
- Stripe hosted checkout is coded but disabled by default. Real MySQL, provider payments, refunds, SMTP and shared-host Apache end-to-end testing remain outstanding.
- No fake live prices, stock, reviews or store hours.

Start sessions with [SESSION_HANDOFF.md](SESSION_HANDOFF.md).

## Current v2 staging release (2026-10-11)
The user added reversible ZIP upgrades, emergency recovery, organized payments/testing, checkout signup and a wider admin. Read [v2 handoff and verified limitations](docs/CLASSIC_STOREFRONT_V2_ROLLBACK_AND_PAYMENTS.md) **before** working. v2 ZIP binaries/source are currently conversation downloads, NOT yet GitHub code. Do not enable external payment processors without real credential/sandbox/Webhook verification.

## v2.8 Catalog Review milestone (2026-10-11)
See [v2.8 verified build and safety handoff](docs/CLASSIC_STOREFRONT_V2_8_CATALOG_APPROVAL.md). This adds an authenticated, paginated review-and-publish center, exact original-store preview → published product linking and an admin-updater-compatible ZIP with verified file rollback tests. All currently imported source products stay browse-only and do NOT represent confirmed stock until merchant review. v2.8 executable PHP/ZIP assets are still only in this conversation's downloads and must be synced to the repository; real PDO MySQL and production checkout remain untested.


## Current staging hotfix — v2.9.1 (not deployed)
Admin Products now includes imported source candidates and stored drafts, guarded manual `DEMO-` sample cleanup, and 31 observed original-shop categories plus eight verified child categories in admin, Shop and a homepage directory. Existing storefront remains navy/gold/ivory and **non-3D**. The exact source ZIP and admin update archive are conversation artifacts, **not yet GitHub executable source**, and real merchant MySQL/Apache tests remain open. Read [v2.9.1 handoff](docs/CLASSIC_STOREFRONT_V2_9_1_ADMIN_CATEGORIES.md) before resuming.


## Current streamlined design release — v2.9.3 (local staging, not live)
13 visual departments, **58 curated subcategory tiles** rather than 103, with transparent category art, customer-facing department pages, admin editor, 45 stable legacy-slug redirects, preserved product/source mappings, and **no manually typed SHA-256 needed for future upgrade ZIPs** (internal checks/rollback still required). The one-time quick-upgrader manually replaces an older SHA-required updater PHP. **Actual v2.9.3 executable PHP/image assets are in conversation downloads, NOT fully GitHub-synced.** Read [v2.9.3 handoff](docs/CLASSIC_STOREFRONT_V2_9_3_STREAMLINED_CATEGORIES.md) before next work session. Keep non-3D classic storefront scope.


## Current staged improvement — v2.9.4 (not live)
Fixed broad imported original-store records missing from individual subcategory pages; 114/114 historical browse-only records now classify into specific subcategories based on original category and identifiable product-type title. Explicit admin product-to-subcategory assignment/backfill remains protected, existing sale/stock rules unchanged. Replaced identical cropped subcategory images with 58 uniquely referenced padded transparent category-art files and `object-fit:contain` without hover zoom. Some category art still needs editorial review; no claim of exact-SKU photos. Upgrader keeps optional external SHA and mandatory internal integrity checks. **Actual v2.9.4 executable source is in conversation ZIPs, not fully synced to this branch.** See [v2.9.4 handoff](docs/CLASSIC_STOREFRONT_V2_9_4_SUBCATEGORY_LINKS_AND_IMAGES.md).


## v2.9.5 storage repair — one-time host File Manager fix
If the admin ZIP updater reports no writable PRIVATE directory outside the website, use the [v2.9.5 recovery storage repair](docs/CLASSIC_STOREFRONT_V2_9_5_PRIVATE_STORAGE_FIX.md) before retrying v2.9.4. The manual patch upgrades private-directory discovery, adds a storage-check button and preserves all rollback safeguards. It has passed isolated tests, NOT live-host MySQL or permission verification. This is a non-3D PHP storefront; no 3D reinstatement.


## Most recent local staging build — v2.9.8 (NOT DEPLOYED)
Public Shop category cards and filters hide empty departments and subcategories; admin still retains all 13 parents/58 children. Local source snapshot has 6 parents and 15 children visible. Direct URLs for empty categories return 404; no related-product substitution. All 21 visible nodes use materially different 800x620 transparent built-in category art paths, including category-correct accessory illustrations; user-uploaded MySQL category photos still override and can be reset individually to built-ins. 109 PHP + local real-PHP fake-DB HTTP + Chromium 1440/390 checks pass, no real merchant DB/live test. **Complete PHP/WebP source remains in conversation ZIPs, not this GitHub branch.** Read [v2.9.8 handoff](docs/CLASSIC_STOREFRONT_V2_9_8_POPULATED_CATEGORIES.md). NON-3D storefront only.


## Current visual asset milestone — v2.9.9 (staging, not deployed)
New ImageGen batch: 11 standalone transparent PNG subjects, normalized to 11 unique 800×620 RGBA WebPs. 10 category default art paths updated for Guitars, Bass, Amps, Ukuleles, Strings and Accessories plus future visible category paths; hidden empty categories remain hidden. Non-guitar departments still need separate subject-specific original replacements; do NOT treat this as 21/21 completed. User wants full uncropped objects, equal card canvases and photorealism. Categories and products still follow v2.9.8. Source/executable ZIPs in conversation artifacts, not fully committed to GitHub. [v2.9.9 handoff](docs/CLASSIC_STOREFRONT_V2_9_9_ORIGINAL_CUTOUTS.md). NON-3D storefront only.


## Latest local artwork checkpoint v2.9.10 (not live)
Four new transparent 800×620 grouped illustrations have been composed from individually generated v2.9.9 guitar/accessory cutouts and mapped to Guitars & Basses, Folk & Traditional, Accessories, and Folk Accessories. This fixes **two old public category images**, refreshes two parent groupings, and leaves eleven other older visible category artworks for separate approval: do NOT claim all have been replaced. No new 3D, stock, database, installer or payment changes. PHP/visibility/navigation and offline browser tests pass; live host unverified. Executable PHP/WebP remains in conversation ZIPs, not completely synced to this GitHub branch. See [v2.9.10 handoff](docs/CLASSIC_STOREFRONT_V2_9_10_GROUPED_CATEGORY_ARTWORK.md).


## Latest local v2.9.11 image repair (not live)
21 new/reframed 800×620 transparent WebPs replace all 11 remaining older **public** category image paths and also prepare 10 other future categories; each of the 21 currently populated public cards has unique valid art and a missing-custom-image-to-built-in fallback. Three public accessory pictures are reframed inherited illustrations, **not yet brand-new photorealistic artwork**. Unpopulated categories stay hidden; 13 parent/58 child taxonomy and non-3D PHP shop remain intact. 109 PHP lint / 5 JS syntax / 21-image Chromium desktop and mobile / PHP catalog HTTP / ZIP tests PASS locally; real host and MySQL not verified. Executable source and binaries exist as conversation ZIPs, not fully synced here. [Read v2.9.11 handoff](docs/CLASSIC_STOREFRONT_V2_9_11_COMPLETE_VISIBLE_ART.md).


## Latest local v2.9.12 routing repair (not deployed)
Merchant reported Page Not Found and products not opening after v2.9.11. Root cause: safe existing-site ZIP protected old `.htaccess`/`app/bootstrap.php`, while storefront links assumed those files knew the new folder routes. Local v2.9.12 sends every menu/product/asset link directly to `/shop/`, `/pages/`, or `/api/` PHP files and provides 13 simple legacy root compatibility shims; 16-hex original-source product IDs now open browse-only previews, never real checkout. Real PHP HTTP tests with deliberately OLD bootstrap and no mod_rewrite, nested-install prefixes, source catalog, 122 PHP lint and ZIP checks pass. **Merchant live PHP/MySQL hosting not verified.** Exact ZIPs/source exist in conversation artifacts and are NOT yet fully GitHub source-synced. Read [v2.9.12 route recovery handoff](docs/CLASSIC_STOREFRONT_V2_9_12_ROUTE_PRODUCT_RECOVERY.md). Never reintroduce 3D or overwrite installed config, installer, backups or customer data.


## Latest local v2.9.13 diagnostic checkpoint (live demo NOT verified)
Merchant explicitly corrected the staging root to **https://demo.privoralabs.com/prof/** and reports /prof/shop/catalog.php?category=Used missing/categories absent. External browsing from assistant environment cannot access staging; do NOT assert the site is down. An isolated real PHP local HTTP test within literal /prof confirms canonical catalog, Used bookmarked URL, Pages and both test probes return HTTP 200 even with old bootstrap/no rewrites; 124 PHP scripts lint cleanly. Source snapshot contains 114 browse-only listings and no Used records. A **temporary, private-token, read-only diagnostic ZIP** checks live file existence, PHP/database and route HTTP statuses when manually uploaded to /prof; remove diagnostic files immediately after use. Used nav now hides when no listing; full site ZIP contains /shop/catalog.php. Live production failure cannot be identified conclusively without server diagnostic. See [v2.9.13 handoff](docs/CLASSIC_STOREFRONT_V2_9_13_PROF_DEPLOYMENT_CHECK.md). All executable code in conversation ZIPs, not fully GitHub-synced. No 3D work.


## Current urgent staging incident — v2.9.14 (not live verified)
At **https://demo.privoralabs.com/prof/** homepage stops while rendering Shop by Department and /prof/shop/ routes return HTTP 500. Web and runtime DNS cannot reach the user's site; actual host PHP error is unknown. Local v2.9.14 patch catches PHP category-stack exceptions, bundles verified taxonomy fallback, keeps Shop browse-only original store listings available if the full catalog crashes, and writes `ERNY_SHOP_CATALOG_EXCEPTION`/homepage markers to PHP error log. **SIX literal /prof local HTTP cases pass**, including corrupted/missing category dependencies and injected SQL exceptions. Deliverable 70 KB emergency ZIP + 35 MB existing-site ZIP; neither uploaded to host. Never claim full live fix until merchant verifies route and shares PHP error log. See [v2.9.14 recovery handoff](docs/CLASSIC_STOREFRONT_V2_9_14_HTTP500_RECOVERY.md). All executable files remain conversation ZIPs, not fully in GitHub. Keep the non-3D storefront, customer SQL and installed config untouched.


## v2.9.15 verified local recovery (not deployed)
User rejected root PHP compatibility shims and reported missing category/image assets. **Only index.php remains root PHP** in the repaired full ZIP; public modules remain in proper shop/pages/api/admin folders. Admin now exposes all configured 13 main / 58 subcategories, including hidden/empty, plus authenticated Category & Image Health; public only shows populated categories. Active products survive optional schema mismatch and all 71 taxonomy image URLs are present, with /prof-aware fallback JS. Full existing-site ZIP + 96-file targeted ZIP tested after extraction under literal /prof against an isolated PHP fake DB: homepage/Shop/pages/admin HTTP 200, 71 assets HTTP 200, v2.9.14 emergency fallbacks intact; offline Chromium rendering 1440/390 PASS. **Live merchant PHP/MySQL not verified**. Prior root shim files from already-installed versions are not automatically deleted by ZIP extraction; Admin > Organize Root Files safely audits byte-exact shims for explicit cleanup. [Read v2.9.15 handoff](docs/CLASSIC_STOREFRONT_V2_9_15_ORGANIZED_CATEGORY_REPAIR.md). Executable code remains in conversation download ZIPs, not fully GitHub-synced. No 3D.
