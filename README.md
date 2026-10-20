# Shoply Apps website

The website for shoplyapps.com. **This repo is public:** never commit passwords, keys or `.env` files.

## How it goes live
cPanel clones this repo (Git Version Control, path `repositories/Website`). To publish:
1. In cPanel, open **Git Version Control → Manage → Pull or Deploy**.
2. Click **Update from Remote**, then **Deploy HEAD Commit**.

`.cpanel.yml` (still to add, once the site's folder is confirmed) tells cPanel which files to copy into the site's folder.

## Working together
Every change goes on its own branch and PR, never straight to `main`.
