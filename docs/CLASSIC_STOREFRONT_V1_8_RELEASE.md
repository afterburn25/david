# Prof Erny's Music — v1.8.0 Combined Retail Release (2026-10-11)

## User-approved current project scope
The **ordinary PHP/MySQL online music store**, not the previous DAVID 3D showroom. Keep approved transparent Prof Erny's logo, gold-on-navy fleur-de-lis favicon, navy/gold/ivory branding, full-instrument transparent category photography, Home/Shop/Used/School/Rentals/Repairs/About/Contact glossy active navigation, and one unified header search bar.

## Implementation completed locally
Combined v1.3–1.8 release candidate:
- v1.3 unified live search, catalog filters, multiple product gallery images, zoom, compare, updated cart quantity control.
- v1.4 separate customer accounts/password reset, order history and wishlists; admin sign-in remains separate.
- v1.5 guest order requests plus **disabled-by-default optional Stripe hosted checkout** with server-calculated totals, signed webhook and replay handling. Taxes and merchant credential configuration are mandatory before even attempting payment.
- v1.6 inventory CSV/adjustments, fulfillment-driven stock, coupons for requests, reporting, content manager and disabled-by-default email outbox.
- v1.7 instrument finder, school lists, repair photo intake and private status tracking.
- v1.8 SEO XML sitemap/robots/canonical/product JSON-LD, audit/login throttling, authenticated snapshot export, additive migration screen, hidden-product image privacy guard.
- Cart quantity update UI, corrected conditional payment language and private draft image access tests.
- PHP source remains organized: root index.php; shop/, pages/, api/, customer/, app/, admin/, install/, assets/, config/, storage/, docs/.

## Release artifacts (download from originating ChatGPT conversation, not yet GitHub blobs)
- `prof-ernys-music-php-v1.8.0-SAFE-UPGRADE.zip` (3,382,442 bytes)
- `prof-ernys-music-php-v1.8.0-FRESH-INSTALL.zip` (3,399,512 bytes)
- `prof-ernys-music-php-v1.8.0-SOURCE-AND-TESTS.zip` (3,413,321 bytes)
- `prof-ernys-v1.8.0-RELEASE-MANIFEST.json` with SHA-256 checksums

The v1.8 PHP source and binaries have **NOT YET been committed to GitHub**. This doc is the tracked handoff, not a claim of fully reproducible GitHub source.

## Verification performed
- PHP syntax: 64 scripts PASS. JS syntax PASS.
- Installer GET/CSRF/five-step wizard, synthetic PHP storefront render, branded logo and category cutout alpha: PASS.
- Chromium **offline fixture** at 1440 and 390px: unified search visual alignment, keyboard suggestions, active nav, mobile menu, no horizontal overflow: PASS.
- Migrations create-only and ALTER column guards static checks: PASS. Signed webhook HMAC basic positive/negative time-window tests: PASS.
- Privacy regression using isolated PHP HTTP fake-DB fixture: hidden public product/gallery photo 404, active photo served, staff-only cache private: PASS.
- Simulated ZIP merge from v1.2.2 to v1.8 preserved config/database.php, app/bootstrap.php, install/index.php, storage marker and added new modules: PASS.
- Safe ZIP excludes installer, config, storage, upgrade SQL, system installed page, and bootstrap. Complete PHP ZIP integrity PASS.

## NOT tested or certified
The build environment lacks PDO_MySQL and a real MariaDB instance. No live MySQL install, migrations, checkout/inventory/repair end-to-end flows, live Stripe payments/webhook transmission, hosting-specific Apache rewrite/permission tests or transactional-mail delivery were performed. **Do NOT enable payments or claim production certification.**

## Next implementation priorities
1. Sync **exact** v1.8 source and asset hashes to this branch (avoid secrets or live database).
2. Perform real staging MySQL migration and smoke flows; validate shared-hosting Apache, subfolder rewrites and preservation of installed configuration.
3. Run real Stripe test-mode end-to-end checkout + webhook reconciliation and merchant/tax approval **before any live payment activation**.
4. Test email/repair link delivery and sensitive data handling, customer onboarding, accessibility and cross-device checkout.
5. Keep all production data safe. Never run fresh installer over an installed database; back up both files and MySQL first.

## Future sessions
Read this and docs/CLASSIC_STOREFRONT_V1_1_STRUCTURE.md, docs/CLASSIC_STOREFRONT_V1_2_CONTENT_AND_NAV.md, docs/CLASSIC_STOREFRONT_V1_2_1_CATEGORY_MEDIA.md, docs/CLASSIC_STOREFRONT_V1_2_2_BRANDED_FAVICON.md. Do not revert to 3D scope.
