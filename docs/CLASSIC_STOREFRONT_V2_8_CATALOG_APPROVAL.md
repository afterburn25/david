# Prof Erny's Music — v2.8.0 Catalog Review & Canonical Publication

**Date:** October 11, 2026. **Scope:** user-approved conventional PHP/MySQL music retailer, not the historical DAVID 3D experiment. Continue from v2.7.1 visible-source listing base and the v2.0 updater/recovery foundation.

## Real code delivered as conversation artifacts
The **v2.8.0 development code and ZIP binaries exist as current-session downloadable files**, not yet committed to this GitHub branch. A documentation commit does not mean executable source is synced.

- `prof-ernys-music-v2.8.0-CATALOG-REVIEW-HOTFIX.zip`: **41,561 bytes**, SHA256 `f6d17d4f72b13501477e34acbe314b83530c9b3ce8e43002c5815d9c406fc3e4`. 12-file changed-code patch for verified v2.7.1 installs; file-manager extraction.
- `prof-ernys-music-v2.8.0-ADMIN-UPDATER.zip`: **42,483 bytes**, SHA256 `e81a5c869ad20a633c4838541512352f999694559f6ea33d5ac6124af3cecfed`. Contains `erny-release.json` with 12 SHA256-pinned files, **migrations=[]**. Works with existing v2.0 `/admin/upgrade-center.php` format.
- `prof-ernys-music-v2.8.0-FRESH-INSTALL.zip`: **3,482,847 bytes**, SHA256 `310e8b950628181123ecfc646fa3409ed75bff2cabfb54b4799676717df9a9bf`. For **new empty** database only, not for existing installs.
- `prof-ernys-music-v2.8.0-SOURCE-AND-TESTS.zip`: **4,119,966 bytes**, SHA256 `159d6df6d7182b8d040c645b4e31db50382384d6a351800ce38a50ababc351f3`. Includes all local source/test evidence.
- `prof-ernys-music-v2.8.0-SHA256.json`: checksums/manifest for those releases.

## New functionality
- `admin/catalog-publish-v28.php`: authenticated, CSRF-protected, navy/gold review & publication experience. Catalog-draft, published, all-imported views, 24 products/page and aggregate counts across imported products (avoids prior 150-record admin display cap).
- `app/catalog_publish_v28.php`: transaction/row-lock-based approval of imported hidden drafts only. Admin manually types CURRENT price and physically confirmed stock; must independently affirm exact product/variant, current price, physical quantity, and rights-cleared accurate primary photograph. Rejects unknown manufacturer, missing photo, unapproved or previously published product; writes audit. Never publishes automatically.
- Canonical mapping only when `catalog_import_candidates.source_key=sha256('public_snapshot|'+record_id)`, linked to an `active` product; no unreliable fuzzy name matching. The 114 legacy source preview JSON records remain inquiry-only while unverified, then disappear once exact imported snapshot record is published. Legacy preview detail route issues 302 to actual active product page. If v2.7 import tables are missing, original browse-only cards remain visible.
- `app/admin_ui.php` adds Review & Publish to widened persistent grouped sidebar.
- `assets/site.css` adds a narrow-mobile header fix and CSS cache bumped to v2.8.0; preserved user-approved transparent fleur-de-lis favicon and uncropped instrument category images.
- No schema changes, no credential changes, no checkout/payment activation.

## Verification (local, not live certification)
- PHP lint: **89 scripts** PASS, JS syntax PASS, icon/category alpha PASS, legacy homepage/installer protection/CSRF smoke PASS.
- `tests/catalog_publish_v28.php`: synthetic PDO accepts exact source linkage, omits published snapshot previews, rejects invalid brand/photo/price/stock/attestations/candidate linkage, succeeds transaction+audit, rejects repeat publish, rollback leaves hidden record intact — PASS.
- `tests/catalog_publish_http_v28.py`: real isolated PHP HTTP with fake PDO, verifies admin UI, CSRF 403, missing confirmation denial, correct admin approval redirect, offline Chromium page visuals at 1440/390 and no horizontal overflow — PASS.
- `tests/source_http_v271.py`: 114 snapshot products, homepage 10 preview cards, search/category/pagination, detail/404 and no checkout for unverified items — PASS.
- Genuine admin-manifest parser validates SHA256 of 12 files using PharData ZIP compatibility driver because this host lacks ZipArchive — PASS.
- Actual ZIP stage/apply/recovery restore in disposable v2.7.1 site using a MOCKED SQL snapshot: all 12 files updated and exact previous bytes restored, new files removed, protected config unchanged, one-time code revoked — PASS.
- ZIP integrity/exclusion checks PASS.

**Not tested:** real MariaDB/PDO MySQL authoring, live stock counts, a complete Squarespace product Export All, manufacturer-authorized real images, production Apache/ZipArchive, card provider sandbox checkout, production HTTPS emergency recovery. Live merchant operation remains unverified.

## Deployment safety
Existing verified **v2.7.1** website: first take full files+SQL backup, then upload v2.8 **hotfix** using File Manager or stage the **ADMIN-UPDATER** ZIP in existing v2.0 upgrade center with official SHA. Confirm its one-time recovery code before apply. Do NOT rerun installer. This release does not automatically change any product stock, price or status.

New/empty DB only: fresh-install package.

Protected from patch: config/, app/bootstrap.php, install/, storage/, recovery/, system/installed.php, customer data. File restoration does not roll back newer customer/order data in SQL.

## Immediate next roadmap
1. Get merchant's Squarespace Export All CSV or temporary authorized Products API access; import full data into drafts with canonical identifiers/variants. The 114 public records are **not verified physical stock**.
2. Obtain written commercial image rights/manufacturer dealer assets, exact match by GTIN or manufacturer+MPN, approve exact product photography.
3. Validate batch importer and new verified publishing with real staging MariaDB/Apache/ZipArchive; stress-test thousands of records and rollback without deleting customer orders.
4. Complete payment processor sandbox/webhook and shipping/tax tests (live modes remain off), test customer workflow and mobile purchasing.
5. Sync exact v2.8 source/binary assets to GitHub branch; documentation alone is insufficient.
