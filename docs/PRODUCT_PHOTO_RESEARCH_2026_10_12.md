# Product image research — October 12, 2026

Project: Prof Erny's Music, **organized conventional PHP/MySQL storefront** on `classic-storefront-v1`. Do not reintroduce the discontinued 3D showroom or legacy root PHP files.

## User request
Identify photographs for real catalog products from their item descriptions/model numbers instead of generic generated category pictures. The local public-catalog snapshot is `assets/data/public-catalog-v271.json` (114 **historical browse-only** products with titles, brands, categories, source page URLs, 2026-10-11 captured data). It does NOT contain full descriptions for every SKU or verified current stock.

## Research findings (private review, NOT live images)
A staged review artifact now covers all 114:
- 8 **manufacturer-hosted photos of the listed model** (7 exact ProTec trumpet-mute models ML203, ML104, ML102, ML201, ML107, ML101, ML100, plus Tagima FS500EQ-BK). Even these require merchant rights authorization and staff visual approval before publishing.
- 5 further manufacturer-hosted image candidates with **finish or variant uncertainty** (Tagima FS700-BK, FS600-BK, FS600 XII-BK, T550 Black and Candy Apple Red). Manufacturer product text sometimes lists Natural while the gallery visibly shows black; never silently assign those images.
- 4 third-party/dealer image URLs (Shure SM57, BETA 52A, BETA 56A and JOYO BantAmp Zombie), explicitly **NOT licensed**; prefer authorized manufacturer/dealer media.
- 21 other entries with manufacturer product-page links but no approved exact image URL selected.
- 76 records still require detailed photo research or merchant-supplied source data.
- Total 17 image candidate URLs, 38 manufacturer product-page links, 114 records with product-title-specific suggested photo searches. These are **research candidate counts**, not photos installed or approved.

## Examples of verified direct manufacturer photo URLs
- ProTec ML203: https://www.protecstyle.com/Protec%20Images/ML203-01.default.jpg?resizeh=1200&resizeid=15&resizew=1200
- ProTec ML104: https://www.protecstyle.com/Protec%20Images/ML104-01.default.jpg?resizeh=1200&resizeid=15&resizew=1200
- ProTec ML102: https://www.protecstyle.com/Protec%20Images/ML102-01.default.jpg?resizeh=1200&resizeid=15&resizew=1200
- Tagima FS500BK: https://tagimaguitars.com/cdn/shop/files/tagima-acoustic-fs500-bk.png?v=1781628891 (requires merchant review)

### Manufacturer model pages
- https://www.protecstyle.com/LIBERTY-TRUMPET-COMPACT-ALUMINUM-PRACTICE-MUTE
- https://tagimaguitars.com/products/fs-500bk-eq
- https://tagimaguitars.com/products/fs-700bk-eq
- https://www.shure.com/en-US/products/microphones/sm57

## Local artifacts generated in the ChatGPT conversation
- `prof-ernys-product-image-research-114.xlsx`: filterable editable 114-product research workbook plus candidate-photo and overview sheets.
- `prof-ernys-product-image-candidates.json`: machine-readable 114 product/photo queue for future review/import, **not a ready-to-publish image mapping**.
- `prof-ernys-photo-candidate-preview.html`: optional standalone candidate image preview loading original third-party URLs.
- `prof-ernys-product-image-research-review-pack.zip`: all of the above with explanatory README.

**Exact workbook, JSON, HTML and bundle are conversation attachments, not GitHub files, and should NOT be claimed committed/executable from this doc.** No executable PHP, product rows, database configuration, media BLOBs, stock, prices, order history, or live website files were altered.

## Next practical step
The strongest complete-coverage source would be the **merchant's authorized Squarespace Export All CSV / media export** or licensed manufacturer dealer asset feeds. Import into the existing authenticated Product Media Review workflow as PENDING, verify exact brand+MPN/model+finish, ensure authorized commercial image rights, then approve one image at a time or through reviewed batches. Never treat historical public listings as on-hand inventory or bypass approval. Maintain the `/prof/` subdirectory deployment, organized PHP folders, non-3D design, and the prior site HTTP-500 diagnostics until the merchant live host is actually confirmed.
