# Working on this repo

- Commit and push straight to `main`. Don't create branches or pull requests unless asked.
- The live site (shoplyapps.com) is deployed by hand from cPanel (see README.md), so pushing to `main` doesn't publish it on its own.

# Mobile layout (check every change on phones)

- Check new or changed pages at phone widths (320, 360 and about 400 px) before pushing: no sideways scrolling, nothing cut off.
- Don't leave an icon or small image alone on its own row with empty space beside it. On phones, put the icon next to its title in one row, with badges, text, tags and buttons full width underneath (see `.app-card`, `.app-head` and `.app-tile`).
- Avoid big empty gaps on phones: use tighter padding and smaller headings than on desktop.
- Phone header shows only the logo plus "Our apps" and "Blog". Don't add more buttons there.
- Images keep their proportions: give every `<img>` `width`/`height` attributes and keep `height: auto` in CSS.
- Long text such as URLs and code must wrap (`overflow-wrap: anywhere`).
- When `assets/blog.css` changes, bump its `?v=` number in every page that links it, so phones load the new styles.
