# Prof Erny's Music v2.9.5 — private ZIP upgrade storage fix

Date: October 11, 2026. This is for the conventional non-3D PHP/MySQL storefront on classic-storefront-v1, not the historical DAVID 3D experiment.

## User-reported blocker
The admin updater displayed: "A persistent, PRIVATE writable directory outside the website is required for safe ZIP updates and recovery. Nothing has been changed."

The old recovery engine only inspected HOME and the immediate parent of the installed website. On nested shared hosting such as public_html/store, both are often publicly served or unwritable, so the updater correctly refused to change files. PHP open_basedir restrictions or PHP-FPM ownership may also independently prevent private storage creation.

## v2.9.5 isolated source repair
- recovery/engine.php now traverses safe ancestors above the website, validates the actual document root, checks the backup location remains outside all publicly served paths, refuses symlinks and temporary directories, restricts its backup directory to 0700 and actively tests PHP write access.
- Previously created safe recovery storage is reused before creating new folders. Optional host-wide ERNY_UPGRADE_PRIVATE_PARENT selects an absolute private parent directory, if set consistently for both admin and independent recovery PHP requests.
- admin/upgrade-center.php adds a CSRF-protected "Check & Prepare Private Backup Folder" action and safe hosting guidance.
- No site files, DB schema, current stock, commerce flows, images, category mapping, customer data or payment settings are changed by the one-time fix. It does not bring back 3D.
- ZIP uploads still do not require the merchant to paste an external SHA-256. Internal file hashes, SQL backups, admin password, restore code and rollback remain mandatory.

## Installing this protected-engine hotfix
The existing admin updater deliberately PROHIBITS modifying recovery/engine.php through a submitted ZIP, so a one-time File Manager extraction is necessary. First back up ALL existing website files and export the real MySQL DB, and save the current engine.php and admin/upgrade-center.php files separately. Upload/extract prof-ernys-v2.9.5-ONE-TIME-PRIVATE-STORAGE-FIX.zip at the already installed site root, replacing only those two PHP files. Do NOT use the normal admin ZIP uploader to install this bootstrap patch. Then open Admin > Upgrade Center, click Check & Prepare Private Backup Folder, and only after it succeeds upload the previous official v2.9.4 ADMIN-UPDATER.zip and save the recovery code before confirming.

If private storage STILL cannot be provisioned, do not bypass checks. The hosting provider must grant PHP a persistent private writable folder OUTSIDE public_html and allow it under open_basedir. Never chmod 777 and never store SQL backup files inside the served website.

## Actual validation, not merchant-site certification
Both PHP files pass PHP 8.4 lint. Nested document-root discovery creates private 0700 storage; changing HOME preserves existing restore-point discovery; public-root overrides, symlinks, /tmp and restrictive open_basedir all fail closed. The genuine engine completed isolated stage/apply/recovery/rollback of a two-file release plus mock SQL backup, then verified all 66 entries of the real v2.9.4 updater ZIP could be installed and rolled back on a fake site. This does not verify real PDO/MySQL, PHP-FPM account identity, actual live host permissions or disaster recovery.

## File/source availability
The verified one-time patch ZIP is a ChatGPT conversation file: prof-ernys-v2.9.5-ONE-TIME-PRIVATE-STORAGE-FIX.zip, 14,037 bytes, SHA256 305952c3dbdb5306792cd6a0f1274f3720f0b927612ed5e614f7eb745b7616bd. Contents: recovery/engine.php, admin/upgrade-center.php, INSTALL-ONE-TIME-STORAGE-FIX.txt. Actual executable PHP remains in the conversation file; GitHub has this handoff DOCUMENT ONLY, not the full source release.
