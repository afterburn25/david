# Prof Erny's Music — conventional storefront v1.2.0 (2026-10-11)

**Scope locked:** approved navy/gold/ivory conventional PHP/MySQL storefront and transparent PROF ERNY'S MUSIC logo. No 3D showroom. Continue from v1.1 organized root (only `index.php`; `shop/`, `pages/`, `api/`, `app/`, `admin/`, `install/`, `config/` etc).

## Implemented in the downloadable v1.2.0 release

- New **Home** entry in main navigation; eight navigation links styled as glossy navy pills, animated gold hover/focus, gold active page highlight and `aria-current="page"`. Active state is determined from actual PHP executed route, including Used category and nested shop pages.
- Responsive menu uses proper `aria-expanded`, opens/closes reliably and responds to Escape or outside click; reduced-motion styles supported.
- Enhanced homepage with special-order/used and hard-to-find gear story, genuine on-site instrument repairs, Cajun Country history, and real Lafayette contact.
- Correct original-site business information in `app/business.php` as fallback: 1508 South College Road, Lafayette LA 70503; (337) 232-1850; proferny@yahoo.com; business founded circa 1940 by clarinetist/educator Lawrence E. Erny Jr., family tradition and current Erny family. Suppresses ONLY known incorrect Metairie/504/demo email examples; other merchant settings never overwritten.
- New About page and enhanced Contact with verified content; shipping/returns overview based on current published policy and explicitly pending store approval; current product category filters include Folk/Cajun and Pro Audio.
- Store Settings includes CSRF-protected opt-in import of verified public business details that changes only missing fields or exact known legacy placeholders. Store hours not guessed.
- New `admin/source-import.php` provides five curated original-site products as HIDDEN and stock-zero drafts only, with source links and snapshot prices clearly requiring confirmation. No automatic saleable product imports or image copying.
- Fresh browser installer pre-fills the verified contact defaults and leaves hours blank. Five-step installer and its security logic are otherwise maintained.

## Delivered artifacts in originating conversation

- `prof-ernys-music-php-v1.2.0-SAFE-UPGRADE.zip` (for existing v1.1 install, 2.56 MB).
- `prof-ernys-music-php-v1.2.0-FRESH-INSTALL.zip` (for empty DB, 2.58 MB).

Both ZIPs were programmatically created and SHA-256/integrity/exclusion validated. **The PHP source files and ZIP binaries have not been committed to this GitHub branch**; the downloadable conversation artifacts are the authoritative v1.2.0 build until source sync. This documentation is committed for future handoff.

## Validation

- PHP lint all 34 PHP scripts: PASS.
- Node static JS syntax: PASS.
- Root/legacy route, URL helper, installer HTTP GET/CSRF/5 stages: PASS.
- Real PHP fake-database homepage with verified content and 8 nav buttons: PASS.
- 11 PHP route-current/aria-current navigation cases and fallback suppression: PASS.
- Chromium **offline self-contained HTML** desktop/mobile: active Home, hover gradients, menu toggle and Escape: PASS. Localhost navigation is blocked by test environment; this is not an end-to-end live server browser test.
- ZIP integrity, root layout and preservation of config/install/storage/bootstrap from safe upgrade: PASS.

**Not validated:** real shared-host Apache behavior, live MySQL product draft importer and checkout, old site content bulk migration, current prices/stock, live payments (checkout remains order-request), policy approval, real store hours.

## Source of truth for content

- https://proferny.com/ — location, repair and unique-gear strengths.
- https://proferny.com/about — founder circa 1940, school-band legacy, David and Mary Erny family story.
- https://proferny.com/contact — address, phone, email.
- https://proferny.com/shop — bands, guitars, percussion, accessories, folk, pro audio, used and Cajun categories.
- https://proferny.com/shipping-returns — policy overview pending operator review.

## Critical next steps

1. Sync v1.2.0 source and approved logo into this branch **safely**, never commit live DB config/secrets.
2. Test with staging MySQL and cPanel/Apache rewrite/subfolder paths and permissions.
3. Verify original catalog migration scope and authorized product photos; keep import drafts hidden/stock zero until reviewed.
4. Test checkout, order and repair workflows end-to-end, and obtain merchant approval for shipping/returns and hours.
5. Continue focusing on conventional high-converting shopping and existing full-stack PHP, not 3D.
