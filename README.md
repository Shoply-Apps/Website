# Shoply Apps website

The website for shoplyapps.com. **This repo is public:** never commit passwords, keys or `.env` files.

## How it goes live
cPanel clones this repo (Git Version Control, path `repositories/Website`). To publish:
1. In cPanel, open **Git Version Control → Manage → Pull or Deploy**.
2. Click **Update from Remote**, then **Deploy HEAD Commit**.

`.cpanel.yml` tells cPanel which files to copy into `public_html` (the folder shoplyapps.com is served from). When you add a new file or folder to the site, add it to `.cpanel.yml` too.

## Working together
Changes are committed and pushed straight to `main` (see `CLAUDE.md`).

## Server rules
`server-rules.htaccess` holds recommended Apache rules (404 page, https/non-www redirect, compression, caching). They are not deployed automatically: paste them at the top of `public_html/.htaccess` in cPanel File Manager.

## Blog tools
After adding, renaming or removing a guide in `blog/`, run:
```
python3 tools/build_blog_index.py      # blog/index.html (groups are listed at the top of the script)
python3 tools/build_feed.py            # blog/feed.xml
python3 tools/build_homepage_guides.py # guide list used by the homepage's rotating "Free guide" line and daily cards
```

The animated header logo lives in `tools/logo_svg.py`; after changing it run `python3 tools/apply_header_logo.py` (and `tools/build_blog_index.py`).
Also add the guide to `sitemap.xml` and `llms.txt`.
