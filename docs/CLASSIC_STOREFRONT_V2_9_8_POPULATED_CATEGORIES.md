# Prof Erny's Music — v2.9.8 populated-only categories + replacement navigation art
Date: 2026-10-11/12. **Current design remains a conventional navy/gold/ivory PHP/MySQL storefront (NO 3D).** Use branch `classic-storefront-v1`, not historical `main` DAVID showroom.

## User issues fixed in locally built release
- Public main-department and subcategory tiles, as well as Shop filter selectors, now list ONLY categories containing an already active DB product or a real original-store browse-only snapshot record not superseded by published inventory. Hidden imported drafts, `demo` samples and unpopulated taxonomy rows do not count. Empty category direct links return HTTP 404 and show a Shop directory link; the old related-department substitute product section was removed.
- Existing 13 parents/58 children are kept in Admin > Department Manager for subsequent inventory imports; with current 114 browse-only source records and no real DB active stock in the test fixture, exactly 6 parents and 15 children display publicly. Adding a real active matching SKU makes its category visible without code changes.
- Replaced 21 visible category image paths with distinct 800x620 RGBA WebP artwork under `assets/img/visible-category-art-v298`. Earlier cutout screenshots had visibly missing edges. New art includes one standalone AI-generated red electric guitar and further newer isolated illustrations; four matched accessories (reeds, felt ukulele picks, drum-stick bags, microfiber cloths) use clean illustrative graphics. Transparency and no CSS cropping verified in browser, but not all are independently certified photorealistic or manufacturer SKU photos.
- Existing admin-uploaded custom category images stored in the database take precedence over the new built-ins. Use **Admin > Department Manager > Edit Category > Restore Built-in Image** on any category still showing an old custom photo. Do not automatically remove merchant uploads.
- Image URLs changed and CSS query changed to v2.9.8 to avoid browser cache reuse; no database migration or modification of product stock, price or order history.

## Tests
PASS: 109 PHP files lint; 5 JavaScript syntax checks; source/live-category read-only mapping tests; real localhost PHP HTTP with fake PDO for browsing and 404 empty categories; 21 unique, fully transparent 800x620 category cutouts; offline Chromium 1440px/390px, no broken artwork or horizontal scroll. **No real merchant MariaDB/Apache/PHP-FPM or payment certification.**

## Artifacts (created in ChatGPT working session, executable code not yet GitHub-synced)
- `prof-ernys-v2.9.8-FULL-WEBSITE-EXISTING-INSTALL.zip`: 31,947,558 bytes, 399 deployable files, SHA256 `49b4d17c887a75809909b0bbab93a1b6447c567f0b3bc3cad3a5db9778f5d25d`.
- `prof-ernys-v2.9.8-SAFE-CATEGORIES-AND-IMAGES-HOTFIX.zip`: 1,882,155 bytes, 31 category/PHP/CSS/image files, SHA256 `704f20ffa04a7b4c9b8e04076ea75571f98285f5d6996635928cce9b2b675e2c`.
- `prof-ernys-v2.9.8-SOURCE-AND-TESTS.zip`: 48,621,863 bytes, 498 files, SHA256 `f878175c4d557cb517fb4b3b34f3552caac7764216c3210d64b0300579446826`.
- `prof-ernys-v2.9.8-RELEASE-CHECKSUMS.json` tracks file-level hashes. The ZIPs are conversation downloadable files, **NOT yet committed to GitHub as executable source**.

## Hosting-specific deployment
The merchant's PHP updater was blocked by file ownership/permissions; install via **hosting File Manager** after complete website files and MySQL backup, merging only ZIP files into the EXISTING installed site root. Packages exclude `config/`, `app/bootstrap.php`, `recovery/`, `install/`, `storage/`, `admin/upgrade-center.php`, `.htaccess`, and user data. Manual extraction has no automatic rollback, so keep backups. Never run installer on existing store. No typed SHA256 needed for the manual upload. Live MySQL/user-uploaded image precedence remains unverified on the actual host.

Next: synchronize exact executable PHP/WebP files to GitHub, test real MariaDB/Apache category updates, review exact manufacturer product imagery and improve any remaining generic category illustrations.