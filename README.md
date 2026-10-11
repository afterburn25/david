# Prof Erny's Music — Classic Full-Stack PHP Storefront

**Current approved work:** traditional conversion-focused online store on PHP 8.1+/MySQL shared hosting. The DAVID 3D showroom remains a separate historical experiment on main; it is not the current website design.

## Locked brand
- User-approved transparent Prof Erny's navy/gold logo.
- Gold fleur-de-lis favicon on navy.
- Navy, gold, and ivory e-commerce site with Home/Shop/Used & Rare/School Band/Rentals/Repairs/Our Story/Contact active/hover navigation.
- Unified header search, transparent photoreal instrument cutouts with object-fit: contain.
- Professional five-step branded in-browser installer.

## Current release candidate
**v1.8.0** bundles staged v1.3–v1.8 features. Read [release handoff](docs/CLASSIC_STOREFRONT_V1_8_RELEASE.md) and the [organized folder layout](docs/CLASSIC_STOREFRONT_V1_1_STRUCTURE.md).

The built v1.8.0 source and ZIPs exist as downloadable artifacts in the originating ChatGPT conversation, **not yet fully in this GitHub branch**. Do not pretend GitHub hosts the code until it has been synchronized, tested, and verified. The latest actual implementation is a PHP release candidate, not live-commerce certified.

## Shared-hosting requirements and safety
- PHP 8.1+, PDO_MySQL, Apache with .htaccess, HTTPS, MySQL/MariaDB.
- Installed site upgrades **never** overwrite app/bootstrap.php, config/, storage/, install/ or database tables.
- Use safe ZIP with full backups, run authenticated additive /admin/updates.php migrations. Never run the fresh installer on an existing store.
- Stripe hosted checkout is coded but disabled by default. Real MySQL, provider payments, refunds, SMTP and shared-host Apache end-to-end testing remain outstanding.
- No fake live prices, stock, reviews or store hours.

Start sessions with [SESSION_HANDOFF.md](SESSION_HANDOFF.md).
