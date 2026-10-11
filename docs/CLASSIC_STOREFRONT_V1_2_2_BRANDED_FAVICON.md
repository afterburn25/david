# Prof Erny's Music — v1.2.2 Approved Favicon (2026-10-11)

Current locked direction is the **ordinary PHP/MySQL storefront**, not the earlier 3D showroom. Retain the navy/gold/ivory approved design, transparent primary logo, high-conversion pages, and polished five-step browser installer.

## User-approved icon
The user approved the glossy **gold fleur-de-lis on navy square** as the new browser favicon. Source image in originating chat: `glossy_gold_fleur_de_lis_emblem.png`, 1254×1254 RGBA with transparent edges. Do not use the entire horizontal Prof Erny's text logo as the favicon again.

## Implemented in v1.2.2 locally
- Root `favicon.ico`: multi-resolution 16×16, 32×32, 48×48, 64×64.
- `assets/favicons/favicon-16x16.png`, `favicon-32x32.png`, `favicon-48x48.png`, `apple-touch-icon.png` (180×180), `android-chrome-192x192.png`, `android-chrome-512x512.png`; transparent edges retained.
- `assets/favicons/site.webmanifest` with relative `../../index.php` start and scope so subfolder shared hosting remains supported.
- `app/store.php` common PHP head uses proper `rel=icon`, `rel=apple-touch-icon`, and manifest tags with `?v=1.2.2` cache-bust. This covers public shop, product, cart, service and admin screens.
- Fresh-only `install/index.php` wizard head includes the same icon links via `../` relative paths. Existing installations must NOT rerun /install.
- `docs/UPGRADE_v1.2.2.md`; no database changes, no category image changes and no navigation changes.

Three release ZIPs were generated and verified in this conversation:
1. `prof-ernys-music-php-v1.2.2-FAVICON-HOTFIX.zip` (10 files; app/store.php + 8 favicon assets + docs; excludes installer/bootstrap/config, root index and database)
2. `prof-ernys-music-php-v1.2.2-SAFE-UPGRADE.zip` (installed storefront, excludes `app/bootstrap.php`, `config/`, `install/`, `storage/`, `upgrade/`, and `tests/`)
3. `prof-ernys-music-php-v1.2.2-FRESH-INSTALL.zip` (new empty database only; updates wizard favicon).
Bonus: separate standalone favicon asset ZIP.

## Tests completed
- Current PHP release smoke suite: 34 PHP files lint, JS syntax, 11 active-navigation cases, current installer GET/CSRF/5-step render, existing category photo object-fit:contain and alpha pass.
- Favicon 16/32/48/180/192/512 PNG dimensions and RGBA alpha pass; ICO includes 16/32/48/64.
- Real isolated PHP HTTP: `favicon.ico`, 32px icon, Apple icon, 512px icon, JSON manifest served 200; installer includes new icon links.
- Manifest subfolder path sanity; all ZIP integrity tests passed.
- Not tested: live shared-host deployment, browser icon caches on user's machine.

**GitHub note:** These release ZIPs and image binaries are conversation artifacts; the **actual v1.2.2 PHP/image source is not yet committed** to the `classic-storefront-v1` branch. Do not claim otherwise. The image artwork source is not identical to the original logo but the user expressly selected it as favicon.

## Next session
Continue from classic-storefront-v1 and v1.2.2, sync exact source/assets when possible, keep favicon and never revert to logo-as-icon. Verify host Apache and caching on staging. Preserve user data and installer config protections.
