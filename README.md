# Shoply Apps website

The website for https://shoplyapps.com. **This repo is public:** never commit passwords, keys, tokens or `.env` files.

## Where everything lives

| What | Where | Notes |
|---|---|---|
| Code | GitHub: `Shoply-Apps/Website` | `index.html` is the whole homepage (its styles are inside it). |
| Domain | GoDaddy: Domain Portfolio → `shoplyapps.com` | Its nameservers point to Cloudflare. **Don't edit DNS at GoDaddy**: it's ignored. |
| DNS and HTTPS | Cloudflare (free plan): `shoplyapps.com` | All DNS records live here, and Cloudflare provides the HTTPS certificate. |
| Hosting | GoDaddy cPanel, folder `public_html` | Server address `50.62.185.135`. The site is copied here from GitHub. |
| Email | cPanel → Email Accounts: `info@shoplyapps.com` | Read it in Outlook or in cPanel webmail. |

## 1. Get access (once)

Ask Romas for these invitations. Each one gives you your own login, so nobody shares passwords:
1. **GitHub:** membership of the `Shoply-Apps` organization.
2. **GoDaddy (domain and cPanel):** GoDaddy → Account settings → **Delegate access**, invite by email.
3. **Cloudflare:** Cloudflare → Manage account → **Members**, invite by email.

## 2. Get the code (once)

Install Git (https://git-scm.com), then put this repo next to the app's repo:

```bash
git clone https://github.com/Shoply-Apps/Website.git
```

## 3. Make a change

1. Get the latest code and start a branch. Never work on `main` directly:
   ```bash
   git checkout main
   git pull
   git checkout -b fix/short-description
   ```
2. Edit the files:
   - `index.html`: all homepage text and styles.
   - `assets/`: company logo (`shoply-apps-logo.svg`), tab icon (`shoply-apps-favicon.svg`), app icon (`logo.svg`).
   - `privacy.html`, `terms.html`: **don't edit them by hand**, see "Privacy and terms pages" below.
3. Check it: open `index.html` in your browser (double-click it), and check a phone width too (browser dev tools → device toolbar).
4. Commit and push:
   ```bash
   git add -A
   git commit -m "What you changed"
   git push -u origin fix/short-description
   ```
5. Open the link Git prints (`.../pull/new/fix/short-description`), create the pull request, and merge it on GitHub after a look.

**Adding a new file or folder?** Add it to `.cpanel.yml` too, or it won't be copied to the website.

## 4. Publish it

After the pull request is merged:
1. cPanel → **Git Version Control** → `Website` → **Manage** → **Pull or Deploy**.
2. Click **Update from Remote** (fetches the merged code), then **Deploy HEAD Commit** (copies it into `public_html`).
3. Open https://shoplyapps.com and press **Ctrl+Shift+R** to skip the browser's cache.

## Privacy and terms pages

They're generated from the app's legal texts (`docs/legal/*.md` in the app repo), so the website and the app always say the same thing. After those texts change, run this in this repo's folder (with the app repo next to it), then commit `privacy.html` and `terms.html`:

```bash
node tools/build-legal.mjs ../shoply-apps-project-1
```

## Don't

- **Don't click "Publish Site" or use Airo in GoDaddy.** It would put a GoDaddy-built page on the domain.
- **Don't change Cloudflare's SSL/TLS mode.** It must stay **Full**: "Flexible" causes redirect loops, and "Full (strict)" breaks the site, because the hosting only has a self-signed certificate.
- **Don't turn on the orange cloud** in Cloudflare for `mail`, `webmail`, `autoconfig`, `autodiscover` or `_domainconnect`. Email and cPanel need them grey (DNS only).
- **Don't put other files in `public_html`.** Everything on the website comes from this repo.
- **Don't paste passwords or tokens** into chat or this repo. If one leaks, delete it and create a new one.

## Why it's set up this way

- The GitHub organization blocks deploy keys, so cPanel clones this repo over plain HTTPS. That's why the repo is public.
- GoDaddy's cPanel has no AutoSSL, so HTTPS comes from Cloudflare (mode Full).
- The domain used to point to Shopify. GoDaddy support removed that connection and set up the hosting for `shoplyapps.com`.
