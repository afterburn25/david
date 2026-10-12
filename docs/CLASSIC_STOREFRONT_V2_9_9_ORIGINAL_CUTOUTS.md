# Prof Erny's Music v2.9.9 — original transparent category cutouts (2026-10-12)

**Project:** conventional non-3D navy/gold PHP/MySQL storefront. Never return to the abandoned DAVID 3D showroom.

## User request / reason for revision
After v2.9.8, users still saw cropped, inconsistent category illustrations sourced from earlier webpage mockups. User explicitly requested that ChatGPT generate the individual pictures itself and continue. A new batch of 11 distinct high-resolution RGBA PNG **single-subject product category illustrations** was generated for guitars, bass, ukulele, amplifiers, pedals, strings and guitar accessories. Unusable **webpage/contact-sheet** image generations were rejected and are not in the build.

## Actual local implementation
- 11 genuine generated standalone transparent PNG originals, standardized into **11 unique 800×620 RGBA WebP assets** at `assets/img/original-cutouts-v299/`, with safe alpha margins and native proportions preserved.
- Mapped **10** image paths in `assets/data/departments-v292.json`: `guitars-basses`, `electric-guitars`, `acoustic-guitars`, `bass-guitars`, `guitar-amplifiers`, `ukuleles`, `accessories`, `instrument-strings`, `effects-pedals`, `guitar-bass-strings`. An additional Classical Guitar cutout was generated but left unassigned: Classical and Acoustic Guitars are merged into one live subcategory, and no new public category should be invented.
- PHP storefront `app/store.php` bumps stylesheet cache query to v2.9.9; `assets/departments-v292.css` retains `width:100%;height:100%;object-fit:contain`, no hover zoom, with minor responsive media area tuning.
- **Existing v2.9.8 empty-category hiding, source product subcategory mapping, browse-only imported records, admin category editor and saved custom image overrides are preserved.** A custom category image in DB still takes precedence over the new built-in; staff can use Restore Built-in Image. No schema, stock, order, payment or installer changes.
- Images are generic AI-produced category marketing artwork; they **must not be presented as an exact manufacturer's product photo, physical stock or authorized brand image**. Much of the remaining band, percussion, audio and folk category artwork is still from v2.9.8 and needs further dedicated real standalone cutouts. Do not claim all 21 public cards have been replaced.

## Local verification
- 109 PHP lint checks and 5 JS syntax checks passed.
- `tests/category_visibility_v298.php` passed unchanged: 6 populated parent categories, 15 populated child categories with source snapshot, hidden/demo products not counted.
- `tests/generated_cutout_media_v299.py`: 11 unique new 800x620 RGBA WebP files; nontransparent corner detection and alpha subject bbox test, all 10 mapped paths exist, actual 21 visible images load. Chromium desktop 1440px / mobile 390px DOM images and CSS contain + no horizontal overflow: PASS.
- `tests/source_http_v271.py`: actual local PHP server with synthetic PDO confirms original-store browse-only filters, 24/item pagination, one-click subcategory links and empty-category 404: PASS.
- **NOT VERIFIED** against live merchant MySQL, real Apache and permissions, real inventory or current manufacturer image rights.

## Deliverable ZIPs (ChatGPT conversation artifacts; actual binaries NOT yet committed to GitHub)
- `prof-ernys-v2.9.9-GENERATED-CATEGORY-IMAGES.zip`: 11 high-res source PNGs, 11 800x620 WebPs, checkerboard preview and manifest.
- `prof-ernys-v2.9.9-ORIGINAL-IMAGE-HOTFIX.zip`: 15 entries, containing new images, mapping JSON, CSS and cache bump; **recommended** for already installed v2.9.8 existing store.
- `prof-ernys-v2.9.9-FULL-WEBSITE-EXISTING-INSTALL.zip`: 411 files, full conventional existing-site PHP deployment, excludes protected config/bootstrap/recovery/install/storage/.htaccess.
- `prof-ernys-v2.9.9-SOURCE-AND-TESTS.zip`: development/testing archive, not for live extraction.
- `prof-ernys-v2.9.9-RELEASE-CHECKSUMS.json`: artifact SHA-256 digests.

## Safe installation and next work
Hosting PHP updater was blocked by file ownership, so prefer cPanel/File Manager safe-merge ZIP after *full independent site and SQL backups*. Do not delete folders or overwrite protected credentials, private backups/recovery, installer or customer records. Clear browser/CDN cache. Existing database category overrides can hide new built-in visuals until explicitly reset. Next: obtain true isolated cutouts for remaining public Band, Percussion, Pro Audio and Folk categories one-by-one, with real transparency and full-subject quality review; then final image consistency pass against all visible categories. **Do not regenerate website mockups or split images from contact sheets as product assets.**
