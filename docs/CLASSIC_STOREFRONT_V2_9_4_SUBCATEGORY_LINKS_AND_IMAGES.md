# Prof Erny's Music v2.9.4 — Subcategory Product Links and Category Image Presentation
Date: 2026-10-11. Work ONLY on `classic-storefront-v1`, never resurrect DAVID 3D showroom.

## User-reported regression
With v2.9.3's 13/58 category tree, imported products weren't appearing in subcategory search results; several subcategory pictures reused another category or were cropped. User insists images differ by the displayed label and show the whole subject.

## Locally implemented and packaged (NOT deployed)
- `app/categories_v292.php`: deterministic exact-source/category + product-title classifier routes 114 existing browse-only public snapshot records to specific 15 child categories represented in that subset, and parent-scoped browsing includes them. Keeps user-mapped explicit categories and legacy redirects, refuses unknown identities instead of guessing.
- `app/catalog_import_v27.php`: when current mapping tables exist, new hidden imported product candidates may receive a specific category assignment within the existing import transaction; never overrides manual assignments, invents stock, or publishes.
- `admin/products.php`: explicit Store Subcategory dropdown on editor and transactional writes, separate from original raw category.
- `admin/categories-v292.php`: confirmed Classify Unassigned Drafts action uses reliable product-title/source category to assign hidden imported drafts. It does **not** modify active items, quantity, prices or payment state. Merchants must initialize Department Manager tables if absent and explicitly run historical backfill.
- `shop/catalog.php`: source-derived product matching fixed; category product mapping table existence separately checked before SQL lookup.
- `assets/img/subcategories-v294/*.webp`: 58 separate padded RGBA WebP category visuals; `assets/data/departments-v292.json` references unique versioned paths. `assets/departments-v292.css` uses `object-fit:contain` and removes image zoom/crop on hover. Graphic source is earlier generated project art, **not exact manufacturer product photos**. Some composite photos remain illustrative and need merchant editorial replacement/approval.
- Existing navy/gold/ivory conventional storefront, fleur-de-lis branding, no 3D/GLB functionality introduced, and no external 64-character SHA-256 typed for modern ZIP upgrades; internal file hashes/backups/rollback retained.

## Verified in local staging
- 114/114 historical source records classified into 15 represented subcategories, with correct parent membership, read-only semantics and no cross-department leakage.
- PHP lint/synthetic database smoke; simulated real PHP HTTP source catalog and admin products; v2.9.3 legacy redirect tests.
- 58 distinct transparent assets with protective padding, browser containment at 1440px and 390px, no broken images/horizontal overflow.
- v2.9.4 official ZIP parsed and accepted by existing recovery engine's internal manifest checker: 66 files (58 image files + eight PHP/CSS/JSON/docs changes), no SQL migration; forbidden paths excluded.
- Not yet verified against merchant MySQL/Apache, actual stock, exact manufacturer licensed product images, live Stripe/Square/PayPal or HTTPS recovery.

## Available artifacts (current ChatGPT conversation; **not fully committed executable code to GitHub**)
- `prof-ernys-v2.9.4-ADMIN-UPDATER.zip`
- `prof-ernys-v2.9.4-SAFE-MANUAL-HOTFIX.zip`
- `prof-ernys-v2.9.4-SOURCE-AND-TESTS.zip`
- `prof-ernys-v2.9.4-RELEASE-CHECKSUMS.json`

## Deployment
Back up real website files and MySQL first. Apply the official ADMIN-UPDATER via an already installed `/admin/upgrade-center.php`; no manual external SHA. Save recovery code. Do not rerun installer or overwrite `config/`, `app/bootstrap.php`, `install/`, `storage/`, `recovery/`, customer/order files. Then initialize Department Manager's additive mapping tables if needed and choose **Classify Unassigned Drafts** after review; confirm active item mappings manually. Never claim the 114 indexed source items are verified in-stock. Future work: source sync of actual PHP/media, real MySQL test, improve any category composite not visually accurate, and exact manufacturer's images for saleable SKUs.
