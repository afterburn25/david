# v2.9.4 Shared-host file permissions blocker

Date: 2026-10-11. Applies only to the current traditional PHP/MySQL music storefront, not the historical DAVID 3D project.

## Reported user error
`Hosting permissions prevent writing: admin/categories-v292.php; nothing changed.`

## Verified source explanation
`recovery/engine.php` calls `erny_up_path_writable($dest)` from its ZIP stage preflight, which checks the writable state of the destination's **parent directory** via PHP `is_writable(dirname($path))`. This happens before changing application files. PHP needs to create a temporary sibling and atomically rename it over `admin/categories-v292.php`. The failure is therefore a hosting directory write-access, ownership or PHP-user problem, NOT proof that `admin/categories-v292.php` itself needs its mode changed. Further ZIP destinations may be affected too.

## Safe workaround (the already-built v2.9.4 manual ZIP)
The conversation artifact `prof-ernys-v2.9.4-SAFE-MANUAL-HOTFIX.zip` can be uploaded with the hosting provider's File Manager and extracted/merged into the *existing installed site root* after backing up **all site files and the MySQL database**. It contains 66 application files plus a README; all 66 match their corresponding deployment files in the official v2.9.4 admin update ZIP byte-for-byte. CRC passed; excluded `config/`, `install/`, `storage/`, `recovery/`, `app/bootstrap.php`, `.htaccess` and existing customer data. Do **not** extract the ADMIN-UPDATER ZIP manually because its release manifest is for the upgrade engine.

The File Manager extraction must replace only named files and merge directories; never delete entire existing directories, and check whether the file manager's extractor actually overwrote existing files. This manual process bypasses the PHP write barrier but **does not provide automatic rollback**, so the independent file+SQL backup is critical. If the hosting File Manager cannot replace the files either, hosting provider support must repair ownership/permissions.

## Long-term resolution
Ask provider to configure application folder ownership and PHP-FPM/handler identity so PHP can safely write its deployment directories without world-writable permissions. When the hosting account user and PHP run as the same owner, 0755 directories/0644 files are typical. Changing file chmod alone does not make an unwritable parent directory writable. Never chmod 777 or bypass the updater's preflight. The last requested SHA-256 entry remains optional; this error is unrelated to release integrity.

## Verification limits
This conclusion follows from the local v2.9.5 updater source and v2.9.4 archive inspection; the live site's PHP-FPM identity, `open_basedir`, filesystem ACLs, and MariaDB could not be inspected. Stage reports **nothing changed**, consistent with failure before ZIP apply. Do not claim the live site was changed or tested.

## Recommended next steps
1. Backup website files and SQL.
2. Apply v2.9.4 SAFE-MANUAL-HOTFIX using hosting File Manager; or ask host to correct PHP deployment directory write access and retry normal ZIP update.
3. Confirm product subcategories and exact category artwork; apply unassigned imported-draft category classifications only after review.
4. Preserve non-3D design and update branch `classic-storefront-v1` only.
