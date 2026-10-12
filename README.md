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
