# Prof Erny's Music v2.9.10 — grouped transparent category artwork

Date: October 12, 2026. Branch: `classic-storefront-v1`. Continue ONLY the conventional 2D PHP/MySQL navy/gold/ivory shop; the historical DAVID 3D showroom stays discontinued.

## Scope and honest visual status
User requested continued original, photorealistic transparent category pictures, equal visual sizes and complete items. v2.9.9 supplied 11 successful individual image generations used for several guitar/accompanying categories. Repeated follow-on image generation for Band, Drums, Pro Audio and Folk returned **composite contact sheets rather than clean standalone cutouts**; these were rejected as independent per-category source media. Attempts to extract a brass grouping produced a rectangular background and failed visual QA; that asset was likewise excluded.

The v2.9.10 incremental release assembles four **new grouped product-category illustrations from the previously generated individual transparent cutouts**: `guitars-basses`, `folk-traditional`, `accessories`, and `folk-accessories`. These are NOT newly generated official model/SKU photos or independently generated individual Band/Drum/Audio photos. This pass replaces **two remaining older public images** (Folk parent and Folk Accessories child), and refreshes two already-generated parent category images (Guitars/Basses and Accessories). Eleven older visible category artworks still need correctly sourced standalone replacements, especially Band, Brass, Reeds, Cases, Percussion, Microphones, Recording, and Care items. Do not claim a full 21/21 visual replacement.

## Code and asset changes
- Added 4 transparent **800 × 620 RGBA WebP** group assets at `assets/img/generated-groups-v2910/`.
- Updated `assets/data/departments-v292.json` (version 2.9.10) for ONLY those four image paths. No taxonomy labels, category IDs, product mapping, published status, stock or prices changed.
- `app/store.php` increments category CSS cache tag to `?v=2.9.10`.
- No 3D assets, no DB migrations, no payment/config/bootstrap/installer/recovery changes.
- The previous populated-only public category rules (6 parents / 15 children in synthetic original-store snapshot tests), explicit category assignment, direct-click results, hidden/demo product exclusion and admin-editable image precedence remain intact. Admin-uploaded database photos still override the built-in images until staff resets the relevant category art.

## Actual local tests
- 109 PHP scripts lint: PASS.
- `tests/generated_group_media_v2910.py`: four distinct SHA images, all 800×620 RGBA, zero alpha in corners, full subject within margins, new image paths and 13-parent / 58-child stored taxonomy unchanged: PASS.
- Chromium offline responsive cards at desktop 1440px and mobile 390px: all four images load, `object-fit:contain`, no horizontal overflow: PASS.
- `tests/category_visibility_v298.php`: populated-only public categories and proper hidden/demo exclusion: PASS.
- `tests/category_navigation_v297.php`: old broad labels and explicit admin product mappings: PASS.
- `tests/source_http_v271.py`: local PHP HTTP 10 homepage source cards, paginated catalog, filters, safe inquiry-only original-site preview: PASS.
- All 3 final ZIPs CRC and safe-path/included-file integrity: PASS. Complete existing-site deployment has 414 application files; **not tested on merchant's real MariaDB, Apache, PHP-FPM or production filesystem**.

## Downloadable files — current conversation assets, NOT full executable source on GitHub
- `prof-ernys-v2.9.10-GROUPED-ARTWORK-HOTFIX.zip`: 462,928 bytes, SHA256 `b9bcd90f5838944b65ca4b704c1c5e2028418b62c152f26ccf96f1e0066b9ce9`. Contains four WebPs, JSON mapping, app/store.php and readme.
- `prof-ernys-v2.9.10-FULL-WEBSITE-EXISTING-INSTALL.zip`: 33,573,248 bytes, SHA256 `2b7426bece11b8ab6db1c7f59a187223d1cd59ee80c0d7f2837e35e7476b9024`. 414 deployable files plus readme; excludes protected config/, install/, recovery/, storage/, app/bootstrap.php, admin/upgrade-center.php, .htaccess, dev tests and SQL/customer data.
- `prof-ernys-v2.9.10-GROUPED-TRANSPARENT-ARTWORK.zip`: 627,807 bytes, SHA256 `bfb3cd6d78b2f6879c3a1d2fc54ed05e9b1f9f7d968dbdf033261bb1bdc0f765`. Four WebPs with checkerboard preview.
- `prof-ernys-v2.9.10-RELEASE-CHECKSUMS.json`: package integrity and changed-file SHA hashes.

## Deployment
Because the user's PHP upgrade engine previously failed host write permissions on admin/categories-v292.php, use the **small File Manager hotfix** if v2.9.9 is installed, after independently backing up ALL live files and SQL. Merge only named files, never replace directories or run the installer. Manual extraction has no automatic rollback. Clear browser/CDN cache and check the four images. This is an incremental image quality milestone only, **not a claim that all historical image quality issues are resolved**.

## Source-of-truth gap and follow-up
The current GitHub classic branch contains project handoff docs and some older inherited DAVID files; actual recent PHP/WebP source remains in the conversation ZIPs and has NOT been fully synchronized into a reproducible GitHub checkout. Continue to work from the verified v2.9.10 full-site/source artifacts and sync all executable code after sensitive paths have been audited. Prioritize genuinely new isolated original assets for the 11 remaining visible categories; do not crop or rename broken webpage sheets and call them new individual images.
