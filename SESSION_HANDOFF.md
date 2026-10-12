# Mandatory handoff — current classic storefront v1.8.0

## Project and source
User currently wants **Prof Erny's Music NORMAL, non-3D PHP/MySQL website**, built with navy/gold/ivory premium retail layout, approved transparent logo, gold fleur-de-lis favicon, full instrument category cutouts and Home+active/hover glossy navigation. 3D DAVID project history belongs to separate main branch, **DO NOT return to 3D unless user asks**.

Follow `afterburn25/david` **branch classic-storefront-v1** and `docs/CLASSIC_STOREFRONT_V1_8_RELEASE.md`. Older 3D instructions inherited from main are superseded ON THIS BRANCH.

## Actual v1.8.0 integration release candidate (Oct 11 2026)
Staged v1.3–v1.8 features combined: smart unified search, filtered catalog/multi-product galleries/compare, customer accounts/wishlist/order history, guest order requests plus guarded optional Stripe checkout, admin inventory/CSV/reports/coupons/email-outbox/content management, repair tracking/photos, school lists/finder, SEO and privacy/security. Preserve original PHP folder architecture.

Local packaging produced:
- prof-ernys-music-php-v1.8.0-SAFE-UPGRADE.zip
- prof-ernys-music-php-v1.8.0-FRESH-INSTALL.zip
- prof-ernys-music-php-v1.8.0-SOURCE-AND-TESTS.zip
- prof-ernys-v1.8.0-RELEASE-MANIFEST.json

**These exact code files, brand assets and binaries are NOT yet committed here.** The docs specify what to sync. To resume, retrieve the ZIP from the conversation / user, or another verified available source; never recreate it from imaginary files.

## Checks and limitations
Passed: 64 PHP syntax checks, JS syntax, PHP homepage with fake DB, browser installer GET/CSRF wizard, offline Chromium responsive search/nav at 390 and 1440 px, media auth fake-DB HTTP, webhook HMAC signatures basic, simulated upgrade merge protected install/config/bootstrap/storage, ZIP integrity. Production: **NOT CERTIFIED** — no PDO_MySQL/MariaDB in build host and no live provider Stripe, SMTP, Apache/subfolder integration testing.

## Critical deployment protections
- Existing website: full file + SQL backup, SAFE-UPGRADE ZIP only. Confirm site opens without redirecting to /install. Admin /admin/updates.php applies additive migration. Do not overwrite bootstrap/config/data/installer.
- Fresh empty DB only: use fresh-install ZIP with 5-step wizard.
- Stripe payments stay DISABLED until merchant has configured secrets, tax/pickup policy, tested transaction/webhook/reconciliation end-to-end in live-like staging.
- Product inventory, prices, policies and store hours require human verification.

## Next work
Sync the actual source into classic-storefront-v1; test MySQL migration and commerce/account/service flows, staging browser and payment provider; fix regressions and package upgrades safely; keep docs and real test results updated. Do not claim completion without evidence.

## Most recent work — v2.0.0 staging build
Read `docs/CLASSIC_STOREFRONT_V2_ROLLBACK_AND_PAYMENTS.md` first. User explicitly requested **rollback if an update breaks the site**. Local release includes /admin/upgrade-center.php staging/apply with checksum and one-time recovery code and independent /recovery/index.php for emergency file restore (not destructive SQL rewind). Includes persistent private file+SQL backups, PHP parse and ZIP validation, fail-closed permission checks. Local tests of ZIP application/restoration and deliberate migration failure passed; real shared-host MySQL/ZipArchive and live external card providers are NOT tested. v2 code and images are in download ZIPs, NOT yet on this branch. Preserve previous v1.8 instructions for other modules, but prioritize full source sync, secure staging live compatibility, 3-provider integrated payment forms and webhooks, and maintenance/restore reliability. Do NOT return to 3D showroom without new explicit request.

## Current milestone — v2.8.0 catalog review, not yet live (2026-10-11)
Read `docs/CLASSIC_STOREFRONT_V2_8_CATALOG_APPROVAL.md` before working. The user asked to continue roadmap after v2.7.1 public snapshot browseability. The v2.8 local release creates `admin/catalog-publish-v28.php` and `app/catalog_publish_v28.php`, requires exact product photo and rights, independently retyped merchant current price/stock, four checks, atomic PDO transaction & audit, 24-product paged admin review, and replaces duplicate legacy snapshot cards with canonical links ONLY after exact imported product publication. No migration. It adds a mobile header overflow fix. Tested PHP 89 scripts, synthetic PDO data and isolated HTTP CSRF, Chromium offline 1440/390, v2.0 ZIP manifest verification plus **mock SQL** reversible 12-file updater. ZIPs+SHA in originating conversation; code NOT yet fully GitHub-synced. Real MariaDB/Apache, licensed manufacturer photos, full Squarespace export and physical stock still NEED merchant data and staging tests. Do NOT enable live payments or treat browse-only historical records as on-hand inventory. Preserve conventional navy/gold PHP design and all production config/install/recovery/customer records.


## Most recent session — v2.9.1 (staging hotfix, not live)
User reported imported products missing from Admin > Products, asked to remove demo inventory, and required **same departments as https://proferny.com/shop**. Local v2.9.1 fixes add a unified paginated imported candidate/draft/product admin view, CSRF-protected source-to-hidden-draft action, manual audit-safe deletion of untouched zero-stock DEMO starter rows, and 31 confirmed top-level/8 verified child original category labels in admin, Shop and homepage. Five original image category tiles preserved with accurate labels; a collapsible all-departments directory was added. Source photo-pending status and stock approval gates remain unchanged. The exact code, tests and ZIPs exist as conversation Library artifacts, **not yet pushed as executable source**. Read [docs/CLASSIC_STOREFRONT_V2_9_1_ADMIN_CATEGORIES.md](docs/CLASSIC_STOREFRONT_V2_9_1_ADMIN_CATEGORIES.md); tests are synthetic/localhost and production MySQL/host not verified. Continue classic-storefront-v1; DO NOT switch to DAVID 3D or run an existing-site installer.


## Latest development checkpoint — v2.9.3 slim department visual catalog
User asked to MERGE overlapping subcategories while keeping polished photoreal-style transparent art and 13 main departments, and remove manually typed external SHA for quick upgrades. Actual locally tested v2.9.3 **reduces 103 to 58 subcategory cards** across 13 departments, retains 45 legacy URL redirects, preserves DB product categories and old source label mapping, marks ambiguous cross-department labels for staff review, and tests transparent imagery/mobile responsiveness. Admin update accepts trusted official ZIP without a typed SHA, but continues internal manifest SHA/protected-file/backup/recovery verification. A one-time File Manager PHP hotfix is needed if the existing installed updater still requires SHA. SOURCE/ADMIN-UPDATER/MANUAL/ONE-TIME ZIPs and CSV exist as current conversation downloadable files, **not pushed as executable source to this branch**; merchant MySQL and live provider checkout still unverified. Full details [docs/CLASSIC_STOREFRONT_V2_9_3_STREAMLINED_CATEGORIES.md](docs/CLASSIC_STOREFRONT_V2_9_3_STREAMLINED_CATEGORIES.md). Do not switch to 3D or rerun an installed-site installer.


## Most recent local v2.9.4 staging — NOT DEPLOYED
User reported imported listings not connected to subcategories; exact same/cropped subcategory images. Code fix links all 114 original-store public snapshot listings to category children, retains browse-only/not-in-stock constraints, adds explicit Store Subcategory field to Products editor, auto maps *new* hidden imports only when category tables exist and allows confirmed backfill of old hidden imported drafts. Replaced 58 subcategory media paths with distinct padded transparent RGBA WebP composites and image containment CSS; some compositions need merchant photo review. v2.9.4 manifest admin ZIP locally validated against existing updater. Avoid claiming real merchant MySQL or full visual acceptance. **Files are conversation source ZIP only, not fully GitHub executable source.** See [docs/CLASSIC_STOREFRONT_V2_9_4_SUBCATEGORY_LINKS_AND_IMAGES.md](docs/CLASSIC_STOREFRONT_V2_9_4_SUBCATEGORY_LINKS_AND_IMAGES.md). Keep non-3D conventional PHP site and no typed external SHA required.


## v2.9.5 storage repair — one-time host File Manager fix
If the admin ZIP updater reports no writable PRIVATE directory outside the website, use the [v2.9.5 recovery storage repair](docs/CLASSIC_STOREFRONT_V2_9_5_PRIVATE_STORAGE_FIX.md) before retrying v2.9.4. The manual patch upgrades private-directory discovery, adds a storage-check button and preserves all rollback safeguards. It has passed isolated tests, NOT live-host MySQL or permission verification. This is a non-3D PHP storefront; no 3D reinstatement.

The v2.9.5 ZIP must be extracted manually via File Manager at existing site root, because the normal updater intentionally blocks updates to recovery/engine.php. Back up website and DB first; if PHP open_basedir/ownership forbids ALL private writable paths outside public_html, get host support instead of bypassing security. Tests: full actual v2.9.4 66-file ZIP apply/rollback with fake DB PASS. Code artifact still a downloadable conversation ZIP, not committed GitHub executable source.


## Follow-up: hosting PHP cannot write admin/ directory
Live user reports: `Hosting permissions prevent writing: admin/categories-v292.php; nothing changed.` Inspected v2.9.5 source: preflight checks writable *parent directory*, not only target file; the server's PHP deployment user lacks safe atomic-write access. Avoid 777 and avoid bypassing checks. Use verified v2.9.4 SAFE-MANUAL-HOTFIX.zip through host File Manager with independently backed-up website files and SQL, merging paths without deleting existing directories; all 66 application files exactly match the official updater ZIP and exclude protected files, but manual extraction has no automatic rollback. Alternatively ask provider to reconcile PHP-FPM account user and site-folder ownership. See [docs/CLASSIC_STOREFRONT_HOST_PERMISSION_BLOCKER.md](docs/CLASSIC_STOREFRONT_HOST_PERMISSION_BLOCKER.md). The site remains a normal PHP shop, NOT 3D. No production installation has been performed by this assistant.


## Most recent local staging build — v2.9.8 (NOT DEPLOYED)
Public Shop category cards and filters hide empty departments and subcategories; admin still retains all 13 parents/58 children. Local source snapshot has 6 parents and 15 children visible. Direct URLs for empty categories return 404; no related-product substitution. All 21 visible nodes use materially different 800x620 transparent built-in category art paths, including category-correct accessory illustrations; user-uploaded MySQL category photos still override and can be reset individually to built-ins. 109 PHP + local real-PHP fake-DB HTTP + Chromium 1440/390 checks pass, no real merchant DB/live test. **Complete PHP/WebP source remains in conversation ZIPs, not this GitHub branch.** Read [v2.9.8 handoff](docs/CLASSIC_STOREFRONT_V2_9_8_POPULATED_CATEGORIES.md). NON-3D storefront only.


## Current visual asset milestone — v2.9.9 (staging, not deployed)
New ImageGen batch: 11 standalone transparent PNG subjects, normalized to 11 unique 800×620 RGBA WebPs. 10 category default art paths updated for Guitars, Bass, Amps, Ukuleles, Strings and Accessories plus future visible category paths; hidden empty categories remain hidden. Non-guitar departments still need separate subject-specific original replacements; do NOT treat this as 21/21 completed. User wants full uncropped objects, equal card canvases and photorealism. Categories and products still follow v2.9.8. Source/executable ZIPs in conversation artifacts, not fully committed to GitHub. [v2.9.9 handoff](docs/CLASSIC_STOREFRONT_V2_9_9_ORIGINAL_CUTOUTS.md). NON-3D storefront only.


## Latest local artwork checkpoint v2.9.10 (not live)
Four new transparent 800×620 grouped illustrations have been composed from individually generated v2.9.9 guitar/accessory cutouts and mapped to Guitars & Basses, Folk & Traditional, Accessories, and Folk Accessories. This fixes **two old public category images**, refreshes two parent groupings, and leaves eleven other older visible category artworks for separate approval: do NOT claim all have been replaced. No new 3D, stock, database, installer or payment changes. PHP/visibility/navigation and offline browser tests pass; live host unverified. Executable PHP/WebP remains in conversation ZIPs, not completely synced to this GitHub branch. See [v2.9.10 handoff](docs/CLASSIC_STOREFRONT_V2_9_10_GROUPED_CATEGORY_ARTWORK.md).
