# Prof Erny's Music — conventional storefront v1.1.0

**Current user-approved direction:** ordinary, conversion-focused PHP/MySQL commerce website with the polished PROF ERNY'S MUSIC transparent logo, dark navy/gold/ivory design, modern home/catalog/repairs/school band, and the matching five-step branded browser installer. **The 3D showroom is no longer the focus of the current conventional storefront branch.** Keep past 3D work separate.

## Folder structure (implemented in release ZIPs 2026-10-11)

```
/index.php                     only root PHP file
/.htaccess                     headers, folder-based route compatibility
/shop/catalog.php              storefront catalog
/shop/product.php              product detail
/shop/cart.php                 shopping cart
/shop/checkout.php             order request
/shop/order-confirmation.php   confirmation
/pages/about.php,contact.php,repairs.php,rentals.php,school.php
/api/media.php                 real product photo serving
/system/installed.php          install-completion page
/admin/                        admin accounts, products, orders, settings, safe legacy cleanup
/install/                      5-step browser installer, fresh-only
/app/                          PHP bootstrap, business logic, layout
/assets/                       branded CSS/JS/images/logo
/config/                       DB credentials, never overwrite on upgrade
/storage/                      private runtime
/upgrade/                      additive migrations
/docs/, /tests/                protected documentation and regression tests
```

Updated path_url() honors URL folder remapping, the subdirectory deployment prefix and existing query strings. Apache .htaccess rewrites legacy /catalog.php, /cart.php, /repairs.php, /media.php, etc. to their new handlers even when old root files remain after ZIP extraction. New links use canonical folder-based routes.

## Release packages created in originating ChatGPT conversation

- `prof-ernys-music-php-v1.1.0-FRESH-INSTALL.zip` (fresh install only).
- `prof-ernys-music-php-v1.1.0-SAFE-UPGRADE.zip` (existing installation, no config/, install/, storage/).

The ZIPs are conversation artifacts, **NOT YET COMMITTED AS SOURCE OR BINARIES TO THIS GITHUB REPOSITORY**. Do not claim GitHub contains this code until separately synchronized.

## Verification completed

- PHP lint: 30 scripts, all pass.
- Existing release smoke: transparent logo, PHP fake-DB homepage, installer GET+CSRF/5 steps, Node syntax, DB schema safety — pass.
- New route suite: all 12 relocated handlers, root only index.php, PHP URL helper tested for root/subdirectory/Apache legacy, PHP HTTP redirects to installer and GET installer — pass.
- Both ZIPs: archive integrity and exclusion tests pass.

## Deployment rules

**Existing site:** back up database and files, extract SAFE-UPGRADE into existing web root. Verify canonical pages, cart, admin, installer lock. Optionally use admin/clean-root.php (CSRF + admin authorization) to remove only whitelisted legacy root files after confirming replacements exist. Host filesystem restrictions may prevent deletion; never fake success. The upload itself intentionally does not auto-delete old files.

**New site:** extract FRESH-INSTALL into empty web folder, use /install/ once, prevent destructive reinstalls. Preserve database config and private config recovery behavior.

Not yet tested: live shared-host Apache rewrite/cleanup, real MySQL checkout, payment gateway (order request only), in-browser end-to-end account testing.

The next development task should build from the approved normal storefront and this organized v1.1 layout; do not revert to a 3D concept automatically.
