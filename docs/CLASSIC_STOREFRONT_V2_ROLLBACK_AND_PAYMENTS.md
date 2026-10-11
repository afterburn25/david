# Prof Erny's Music — v2.0.0 ZIP Upgrades and Recovery (Oct 11, 2026)

**User-approved current scope:** conventional PHP/MySQL music-retail storefront, NOT the historical 3D demo. Preserve navy/gold/ivory branding, transparent Prof Erny's logo, gold fleur-de-lis favicon, uncropped transparent category instruments, Home-active glossy menu and unified search.

## Implemented in local v2.0.0 STAGING release

- Widened grouped sidebar and collapsible settings.
- Admin payment connectors for Stripe, PayPal and Square, with sandbox/live credentials and read-only API probes. Gateway values are sodium-sealed under a private automatically provisioned master key outside webroot. **Real live PayPal/Square and new on-page card forms remain UNIMPLEMENTED / uncertified.** Existing guarded Stripe hosted checkout is the only coded production payment path, and is disabled unless merchant enables and verifies it. Admin-only internal simulator is credential-free and never charges, marks orders paid or changes stock.
- Optional signup during checkout with 12+ character password, transactionally attached to the new order; customer private order-details and saved address pages, plus existing wishlist/history.
- **Admin /admin/upgrade-center.php**: upload an official release ZIP with `erny-release.json` plus official 64-character SHA-256; manifest/entry SHA validation, reject ZIP traversal, symlinks, malformed PHP, unlisted/oversized files and writes to protected install/config/bootstrap/recovery/storage files; preflight ownership/free space; 0700 private backups outside public webroot; private compressed MySQL snapshot plus old versions of all affected files; one-time 256-bit recovery code and restore ID shown BEFORE the admin password-confirmed apply; atomic per-file replacements; preapproved additive migration allowlist; automatic file restore if installation fails. DOES NOT attempt destructive DB rewind.
- **Standalone /recovery/index.php**: independent of store bootstrap, database or normal admin; emergency rollback requires HTTPS, saved restore ID and one-time 256-bit recovery code; rate-limited, no plaintext code storage; verified SHA256 file restore. Excluded from future update ZIP modifications.
- v2.0 duplicate migration include/fresh schema regression fixed.

## Artifacts packaged locally (NOT COMMITTED to GitHub as source)

- prof-ernys-music-php-v2.0.0-SAFE-UPGRADE.zip
- prof-ernys-music-php-v2.0.0-FRESH-INSTALL.zip
- prof-ernys-music-php-v2.0.0-ADMIN-UPDATER-RELEASE.zip
- prof-ernys-music-php-v2.0.0-SOURCE-AND-TESTS.zip
- prof-ernys-music-v2.0.0-RELEASE-CHECKSUMS.json

The first SAFE-UPGRADE is necessary to install the updater and independent recovery core on previously installed sites. Later manifest-based admin ZIP updates may use the new updater. Do not run the fresh installer on an existing store.

## Locally verified

- PHP lint: 77 scripts, pass.
- v1.8 fake-database homepage and fresh installer GET/CSRF wizard, logo, category alpha and no-cropping smoke, pass.
- Genuine updater-release ZIP via PharData ZIP adapter (this CLI PHP lacks ext-zip): all 109 files SHA-256 validated and PHP syntax parsed.
- Site backup -> apply -> code-authenticated restore of previous PHP and new asset removal, pass.
- Invalid recovery token denied, one-time code revoked, config/installer/recovery overwrite blocked, ZIP path traversal blocked, malformed PHP blocked, pass.
- Deliberately failed post-file-write migration -> automatic file rollback, pass.
- Independent emergency route served HTTP 200 on local PHP server; private sodium gateway key encryption and admin-only internal no-charge simulation, pass.

## NOT verified / production blockers

- Actual shared-host ext-zip/PDO MySQL database snapshots and migrations, Stripe/PayPal/Square SDK checkouts/provider credentials/webhooks, payment settlement, email and real HTTPS recovery route under production hosting have **not** been tested. No claim of production-ready live processing.
- PHP must have genuine application write access and a persistent private nonpublic directory; code cannot bypass hosting ownership. Updater refuses when backups cannot be safely created.
- Live database rollback is deliberately NOT automatic, to avoid losing new orders/customers placed after snapshot. An SQL snapshot is retained privately for reviewed, administrator-assisted restore.

## Next session required

1. Sync complete v2.0 code/binary assets to GitHub branch WITHOUT secrets; the above packages currently exist only as downloadable conversation artifacts.
2. Test clean/upgrade MySQL, streaming SQL snapshot and restoral in staging; simulate a broken homepage and exercise HTTPS recovery independent of DB.
3. Build and certify Stripe embedded form, PayPal JS SDK + server order capture and webhooks, Square Web Payments SDK + Payments API and webhooks, then allow explicit merchant sandbox/live activation. Keep live modes off until tests and taxes/fulfillment merchant approval.
4. Test customer checkout account creation, full product/order and cart flows, screen-size admin sidebar and accessibility.
5. Preserve existing customer records/config/bootstrap/installer on all updates, keep true rollback paths. 
