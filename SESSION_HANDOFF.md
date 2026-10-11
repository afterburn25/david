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
