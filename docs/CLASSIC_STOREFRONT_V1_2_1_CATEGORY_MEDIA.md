# Category photo and crop fix — v1.2.1 (2026-10-11)

The user reported that homepage category images cropped the ends of instruments, and requested photorealistic cutouts with transparency. **The production PHP implementation has been built and tested as downloadable artifacts; code/binary assets have NOT been committed to this branch yet.** Do not revert to `object-fit:cover` or the old SVG thumbnails.

Files modified in the v1.2.1 build:
- `app/store.php`: five real-alpha optimized WebP category asset mappings in `assets/img/categories/`, intrinsic sizes 720×560, CSS+JS cache-busting 1.2.1.
- `assets/site.css`: category image `object-fit:contain`, taller media areas, vertical room for entire instrument silhouettes, navy/gold card styling, responsive two-column mobile with improved heading wrapping, keyboard focus and reduced-motion support.
- `assets/img/categories/{guitars,band-orchestra,keyboards,drums-percussion,accessories}-transparent.webp`: five separately optimized 720x560 photorealistic AI-generated transparent category cutouts (29–82 KB each; actual alpha 0–255).
- `docs/UPGRADE_v1.2.1.md`, `tests/category_media_v121.py` plus README/Release notes.

These are category **illustrations**, NOT photos of actual Prof Erny's stocked merchandise; product-specific image management is unchanged. No verified brand/model/stock claims should be inferred from cutouts.

Created three packages in originating conversation:
- `prof-ernys-music-php-v1.2.1-CATEGORY-HOTFIX.zip`: minimal nine-file fix; excludes root index, SQL, installer, config, bootstrap, storage, customer data.
- `prof-ernys-music-php-v1.2.1-SAFE-UPGRADE.zip`: full code upgrade excluding private/install files.
- `prof-ernys-music-php-v1.2.1-FRESH-INSTALL.zip`: full app with existing 5-stage branded installer for **empty** DB only.

Validation: PHP lint 34 scripts; existing PHP fake-DB homepage, 11 nav cases, organizer/legacy routes, browser installer CSRF smoke tests PASS. New category assets alpha integrity, compressed size, mappings PASS. Chromium headless offline desktop 1440px/mobile 390px rendered all five actual WebPs with `object-fit:contain` and no horizontal overflow. ZIP integrity/exclusions PASS. Live shared-host database/Apache install still untested.

Next: synchronize exact v1.2.1 code/assets safely to this repo, validate staging deployment, obtain permission for authentic product photos if desired. Leave 3D showroom out of ordinary storefront branch.
