# Prof Erny's Music — v2.9.11 visible category artwork and broken-image repair

Date: October 12, 2026. **Approved project: conventional navy/gold PHP/MySQL shop on `classic-storefront-v1`; no 3D showroom.**

## Work completed in local v2.9.11
After v2.9.10 users complained of missing category images and still-cropped photos. Inspection found 11 public category nodes still pointing to older images: Band Instruments, Brass, Reeds, Band Accessories, Drums, Percussion Cases, Pro Audio, Microphones, Recording Gear, Cases & Gig Bags, Cleaning & Care. Individual RGBA image generations from the most recent ChatGPT session have now been inspected for real transparency/full subjects and integrated where appropriate, rather than packaging any failed contact-sheet or fake-alpha background.

- 21 new/reframed **800×620 transparent WebP files** are in `assets/img/category-cutouts-v2911/`. 18 use newly generated source photos, isolated complete instrument regions or compositions; 3 accessory subjects (Reeds, Percussion Cases and Cleaning & Care) are older full-subject illustrations carefully reframed, **not fresh photorealistic images**.
- `assets/data/departments-v292.json` changes 21 built-in artwork paths, including **all 11 remaining older public paths**, plus 10 future-ready hidden categories. The previous v2.9.9–10 original guitar and folk images are preserved. Each of the **21 presently populated public category cards** now resolves to a unique, present and transparently framed file.
- Genuine local pipeline bug fixed: Pillow thumbnail did not enlarge smaller source art, which made items look tiny. v2.9.11 explicitly resizes both up and down to consistent visual occupancy while preserving full subject and padding.
- `app/category_cards_v292.php` now detects missing admin-uploaded custom image URLs and uses the valid built-in category image automatically instead of hiding the image. **Working staff-uploaded custom images still take precedence**, even if visually stale; merchant may use Admin > Department Manager > Restore Built-in Image. No surprise SQL or image deletion.
- `app/store.php` CSS version bump to 2.9.11 for cache freshness, without changing theme colors.
- No changes to category names/IDs (still 13 main/58 subcategories), live inventory, prices, checkout, orders, payment systems, current PHP installer, private backups, or DB. Public navigation remains populated-only: current synthetic original-source catalog shows 6 parents/15 children; empty categories do not display. Historical indexed source records remain browse-only, not physical in-stock claims.

## Validation evidence
- PHP syntax: 109 files PASS, JS syntax: 5 PASS.
- `tests/category_media_v2911.py`: all **71** taxonomy art paths exist, 21 visible art files unique, RGBA transparency/corner and alpha padding checks, exact required 11 replacements, no old public image refs, and CSS maintain contain. PASS.
- Chromium `1440px` and `390px` verifies actual 21 public images load at naturalWidth=800, no overflow, no CSS cropping. Broken custom URL fallback to built-in tested, PASS.
- `tests/category_visibility_v298.php`, `tests/category_navigation_v297.php` PASS (including hidden/demo exclusion and direct child navigation).
- `tests/source_http_v271.py` actual localhost PHP HTTP with fake PDO PASS (homepage and catalog browse-only listings, search, pagination, no checkout).
- Hotfix and full-site ZIP CRC, duplicate-entry, unsafe-path, prohibited 3D and protected-path exclusions PASS, and changed files are byte-identical in hotfix and full.
- NOT tested on merchant's actual Apache/PHP-FPM/MariaDB, dynamic user image DB data, payment processor, or hosting write permissions; user had previous PHP directory ownership failure, so prefer **hosting File Manager** for installation after independent website+SQL backup.

## Conversation deliverables — binaries not in GitHub branch
- `prof-ernys-v2.9.11-CATEGORY-IMAGE-REPAIR-HOTFIX.zip`: 1,811,599 bytes, SHA256 `02d3c5eae25f4db9135835a66c8238cf7c54acf3b44bbc21409c91d3bb984a2f`, 25 deployable changes + README.
- `prof-ernys-v2.9.11-FULL-WEBSITE-EXISTING-INSTALL.zip`: 35,370,825 bytes, SHA256 `b93769094c8e93990f070292c2074fc15be0d0625366a51790ea2166acd6c020`, 436 deployable files + README. Preserves `config/`, `app/bootstrap.php`, `install/`, `recovery/`, `storage/`, `.htaccess`, `admin/upgrade-center.php`, customer/order data.
- `prof-ernys-v2.9.11-TRANSPARENT-CATEGORY-ARTWORK.zip`: 2,148,050 bytes, SHA256 `df948329bf8fbe8bbb08bf5340beab881817590ca073443e5eff390cd5b781b7`, 21 WebPs and checkerboard preview.
- `prof-ernys-v2.9.11-SOURCE-AND-TESTS.zip`: 61,090,895 bytes, SHA256 `df1fcc11e55b90632bd49fd3bbb537d489e68bbd2228836b40939c45549dc2c6`, development only.
- `prof-ernys-v2.9.11-category-preview.jpg`: 21 publicly populated cards displayed over checkerboard.
- `prof-ernys-v2.9.11-RELEASE-CHECKSUMS.json`: file-level hashes.

**Exact executable source and binaries are downloadable in ChatGPT conversation artifacts but are NOT fully synchronized into GitHub; docs commits are not the executable implementation.** Do not claim live deployment, full visual acceptance of the three inherited illustrations, manufacturer-exact SKU photography, or that GitHub clone alone rebuilds v2.9.11.

## Next step
Confirm whether the merchant wants the remaining three accessory illustrations replaced by newly generated photorealistic product-specific cutouts, and verify actual site custom-image overrides and File Manager installation with real MySQL. If the public site still shows old photos, inspect `catalog_categories_v292.image_sha256`, the image endpoint and cache before changing artwork again.
