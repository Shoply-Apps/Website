// Regenerates privacy.html and terms.html from the app's legal texts
// (docs/legal/*.md in the app repo), so the website and the app say the same.
// Usage, from this repo's folder:  node tools/build-legal.mjs ../shoply-apps-project-1
// This folder isn't listed in .cpanel.yml, so it never reaches the website.
import { writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const site = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const appDir = process.argv[2];
if (!appDir) {
  console.error("Give the app repo folder, e.g.: node tools/build-legal.mjs ../shoply-apps-project-1");
  process.exit(1);
}

// legal.server.js reads docs/legal relative to the current folder.
process.chdir(path.resolve(appDir));
const { legalPage } = await import(pathToFileURL(path.resolve("app/lib/legal.server.js")).href);

for (const name of ["privacy", "terms"]) {
  let html = await (await legalPage(name)).text();
  html = html
    .replace(
      "<footer>Item Scan & Analytics by Shoply Apps</footer>",
      '<footer><a href="/">← Shoply Apps</a> · Shoply: Item Scan &amp; Analytics</footer>',
    )
    .replace(
      '<meta name="viewport"',
      '<link rel="icon" href="assets/shoply-apps-favicon.svg" type="image/svg+xml">\n<meta name="viewport"',
    );
  await writeFile(path.join(site, `${name}.html`), html);
  console.log(`Wrote ${name}.html`);
}
