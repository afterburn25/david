# Prof Erny's Music — v2.6.1 Admin Sidebar Memory and Retail Staging (2026-10-11)

## Scope
The approved conventional PHP/MySQL ecommerce site, **not 3D**, in the locked navy/gold/ivory design with transparent approved logo, gold fleur-de-lis favicon, complete category instrument cutouts and unified header search.

## User-requested admin navigation behavior — IMPLEMENTED LOCALLY
- The PHP sidebar emits **all four nav groups expanded by default on first visit**; progressive enhancement works without JavaScript or storage.
- Save per-group open/closed states and independently scrollable sidebar position to localStorage for future admin page navigations, refresh and same-browser return.
- Admin settings `details.admin-setting-group` state also persists by page to localStorage.
- Session-level, per-URL document scroll position persists to sessionStorage; preserved when revisiting admin pages.
- Added **Expand all** / **Collapse all** shortcuts above sidebar, current active page stays gold with `aria-current="page"`.
- Browser UI storage only; no credentials, customers, payment or inventory values.
- CSS still uses 315px desktop sidebar, one-line item labels; mobile layout retains stacked responsive nav. JS storage-blocked fallback is graceful.

Files changed in local v2.6.1 working tree:
- `app/admin_ui.php`: all-open sidebar, data attributes, control buttons, JS load.
- `assets/js/admin-nav-state.js`: persistent nav and settings state + sidebar/content scroll memory.
- `assets/site.css`: new control styling and accessibility states.
- `app/store.php`: CSS asset cache revision updated to 2.6.1.
- `tests/admin_nav_browser_test.py`: Chromium DOM test using actual PHP-rendered sidebar fixture.
- `docs/UPGRADE_v2.6.1.md`, README and RELEASE_STATUS.

## Release archives produced in originating conversation
- `prof-ernys-music-v2.0-ADMIN-SIDEBAR-MEMORY-HOTFIX.zip` — 4 files; small no-DB/admin-only patch for v2.0.
- `prof-ernys-music-php-v2.6.1-SAFE-UPGRADE-STAGING.zip` — 151 files, ~3.45 MB. Excludes `config/`, `install/`, `storage/`, `recovery/`, `app/bootstrap.php`, `system/installed.php`, `upgrade/`, root `.htaccess` and tests.
- `prof-ernys-music-php-v2.6.1-FRESH-INSTALL-STAGING.zip` — for **new empty** database only.
- `prof-ernys-music-php-v2.6.1-SOURCE-AND-TESTS.zip` — full source/tests.
- `prof-ernys-music-php-v2.6.1-STAGING-RELEASE-CHECKSUMS.json` — SHA256 checksums.

**IMPORTANT GitHub limitation:** the archives and full v2.6.1 implementation currently exist in the originating ChatGPT conversation **but are not fully committed to GitHub**. This document is the handoff for full source sync; do not claim GitHub can build/serve v2.6.1 until exact source has been committed and CI verified.

## Validation evidence
- 106 PHP scripts linted; Node JS syntax clean; storefront + installer synthetic PHP runtime and real HTTP GET/CSRF wizard smoke PASS.
- Active storefront navigation, URL routing, five category photo alpha/non-cropping, favicon regression PASS.
- Chromium rendered actual PHP-admin sidebar markup through `page.set_content` and simulated browser storage reset: default all open, 4 collapse/expand states, localStorage nav+settings and scroll, session document scroll, active Order Management and 390px layout PASS (zero page exceptions). The sandbox blocks direct navigation to HTTP/file URLs, so real navigation/reload on actual host is NOT verified.
- Existing rollback suites PASS with required test ZIP: file restore, one-time recovery code, protected paths, malformed PHP ZIP, deliberate failed database migration automatic **file** rollback. These use mocked DB backup, **not actual MySQL**.
- All archive integrity checked and dry-run ZIP extraction verified it cannot overwrite installed DB config, app bootstrap, installer, recovery or persistent storage sentinels.
- Historical category test expected stale v2.0 CSS cache version; updated to v2.6.1 after test failure.

## v2.1–v2.6 features in staged working tree
Customer email verification and account profile; order stock holds, shipping/delivery and fulfillment records, returns; rental/special-order requests, repair estimate approvals; back-in-stock alerts, moderated reviews, opt-in events; staff MFA, site health, cron notifications, optional PayPal/Square embedded SDK and Stripe guarded checkout. **These are staging code, not live-commerce-certified integrations**.

## Blockers / next
1. Synchronize exact PHP/assets/scripts to GitHub storefront branch with no secrets.
2. Run real MySQL migration and end-to-end cart, payment, account, repair and site health tests under shared-host Apache/PDO MySQL.
3. Verify PayPal/Square/Stripe sandbox payments/webhooks/refunds, tax/shipping merchant configuration, deliverable outbound email, backed-up recovery before live activation.
4. Keep all external payment gateways off and treat v2.6.1 as **staging release candidate**, not final production.
5. Never overwrite user-installed config, installer, storage, recovery or customer data.

## Verified recovery checkpoint after workspace reset
The initial v2.6.1 full-stage archives described above were created in a short-lived working container but **were not uploaded as durable conversation attachments or committed to GitHub before an environment reset**. They are **NOT available as verified downloadable builds**. The original v2.6 implementation is therefore NOT yet a reproducible completed release. Do not invent links to it.

A standalone **v2.0 administrator navigation hotfix** WAS rebuilt and verified from the preserved v2.0 source ZIP, then made available as a conversation download named `prof-ernys-music-v2.0-ADMIN-NAV-PERSISTENCE-HOTFIX.zip` (4 files, SHA-256 `9e21b8d3b84aac97dd60d8d5addfd436aa049fd314e47835c66809e13e12ab23`). It changes only `app/admin_ui.php`, adds `assets/js/admin-nav-state.js`, `assets/js/admin-nav-state.css`, and includes docs. PHP lint and JS syntax pass, and a Chromium offline DOM test passes initial expansion, collapse persistence, sidebar/page scroll, active route, expand/collapse controls, and mobile overflow. Real browser HTTP navigation remains unverified due sandbox restriction.

The next development session should recover or rebuild the v2.1–v2.6 modules from a verified available source and package them **only after actual source and tests are present**. Do not claim the lost package exists. Keep v2.0 hotfix as the recommended current release for this specific sidebar change.
