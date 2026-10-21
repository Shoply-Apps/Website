# Rebuilds blog/index.html from the article folders (titles, descriptions, read times, groups).
# Run: python3 tools/build_blog_index.py
import re, html, json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
groups = [
  ('Choosing Shopify and apps', ['why-use-shopify','essential-shopify-apps-new-store','shoply-item-scan-analytics']),
  ('Starting and growing a Shopify store', ['shopify-store-launch-checklist','how-to-price-products','how-to-start-dropshipping-on-shopify','dropshipping-profit-margins','how-to-find-winning-dropshipping-products','dropshipping-vs-holding-inventory','increase-shopify-conversion-rate','shopify-seo-guide-for-beginners']),
  ('Shipping and checkout', ['shopify-shipping-settings-guide','free-shipping-threshold','reduce-cart-abandonment-shopify','shopify-abandoned-cart-recovery']),
  ('Product pages, photos and email', ['how-to-write-product-descriptions','shopify-product-photography','shopify-product-image-size-guide','shopify-email-marketing-guide','welcome-email-series-ecommerce']),
  ('Social media marketing', ['social-media-marketing-for-shopify','sell-on-instagram-with-shopify','tiktok-marketing-for-shopify','influencer-marketing-small-business']),
  ('Catalog health: pricing, stock and product pages', ['shopify-catalog-health-checklist','shopify-inventory-management','shopify-products-selling-below-cost','shopify-out-of-stock-oversold','shopify-product-page-seo-checklist','google-shopping-product-data-shopify']),
]
order = [s for g in groups for s in g[1]]
posts = []
for slug in order:
    s = open(f'blog/{slug}/index.html').read()
    title = html.unescape(re.search(r'<h1>(.*?)</h1>', s, re.S).group(1)).strip()
    desc = html.unescape(re.search(r'<meta name="description" content="(.*?)">', s).group(1))
    mins = re.search(r'(\d+) min read', s).group(1)
    posts.append((slug, title, desc, mins))
e = lambda x: html.escape(x, quote=True)
ALT = {s: html.unescape(re.search(r'class="post-hero"><img [^>]*alt="([^"]*)"', open(f'blog/{s}/index.html').read()).group(1)) for s in order}
card = lambda slug, t, d, m: f'''      <a class="card" href="/blog/{slug}/">
        <img src="/assets/blog/{slug}.webp" width="1200" height="630" alt="{e(ALT[slug])}" loading="lazy">
        <div>
          <h3>{e(t)}</h3>
          <p>{e(d)}</p>
          <small><time datetime="2026-10-20">20 October 2026</time> · {m} min read</small>
        </div>
      </a>'''
byslug = {p[0]: p for p in posts}
cards = '\n'.join(f'      <h2 class="group">{e(g)}</h2>\n' + '\n'.join(card(*byslug[s]) for s in slugs) for g, slugs in groups)
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "Blog", "@id": "https://shoplyapps.com/blog/#blog", "name": "Shoply Apps blog", "url": "https://shoplyapps.com/blog/",
   "description": "Practical guides for Shopify merchants on dropshipping, pricing and margin, shipping, checkout, product photos, email marketing, conversion, SEO, stock and product pages.",
   "publisher": {"@type": "Organization", "@id": "https://shoplyapps.com/#org", "name": "Shoply Apps", "url": "https://shoplyapps.com/"},
   "blogPost": [{"@type": "BlogPosting", "headline": t, "url": f"https://shoplyapps.com/blog/{slug}/", "datePublished": "2026-10-20"} for slug, t, d, m in posts]},
  {"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://shoplyapps.com/"},
    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://shoplyapps.com/blog/"}]}]}
desc = "Practical Shopify guides on dropshipping, pricing, shipping, product photos, email, social media, SEO and catalog health, from the team behind Shoply Apps."
page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Shopify Guides: Dropshipping, SEO, Marketing | Shoply Apps</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="https://shoplyapps.com/blog/">
  <link rel="icon" href="/assets/shoply-apps-favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#15223d">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Shoply Apps">
  <meta property="og:title" content="Shoply Apps blog: Shopify guides for growing stores">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="https://shoplyapps.com/blog/">
  <meta property="og:image" content="https://shoplyapps.com/assets/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="/assets/blog.css?v=7">
  <script type="application/ld+json">
  {json.dumps(ld, ensure_ascii=False, indent=2).replace(chr(10), chr(10) + '  ')}
  </script>
</head>
<body>
  <header>
    <div class="wrap nav">
      <a class="brand" href="/" aria-label="Shoply Apps home"><picture><source media="(prefers-reduced-motion: no-preference)" srcset="/assets/shoply-apps-logo-animated.svg"><img src="/assets/shoply-apps-logo.svg" width="40" height="40" alt=""></picture>shoply apps</a>
      <ul>
        <li class="keep"><a href="/apps/">Our apps</a></li>
        <li class="keep"><a href="/blog/" aria-current="page">Blog</a></li>
      </ul>
      <a class="btn" href="mailto:info@shoplyapps.com?subject=Keep%20me%20posted%20about%20Shoply%20Apps">Get launch news</a>
    </div>
  </header>

  <main>
    <div class="blog-head">
      <p class="crumbs"><a href="/">Home</a> / Blog</p>
      <h1>Shopify guides for growing stores</h1>
      <p>Practical guides for starting and growing a Shopify store, from dropshipping and pricing to shipping, checkout, photos, email marketing, SEO and catalog health. Written by the team building Shoply: Item Scan &amp; Analytics.</p>
    </div>
    <div class="cards">
{cards}
    </div>
  </main>

  <footer>
    <div class="wrap">
      <div class="foot">
        <a class="brand" href="/" aria-label="Shoply Apps home"><img src="/assets/shoply-apps-logo.svg" width="32" height="32" alt="">shoply apps</a>
        <ul>
          <li class="keep"><a href="/apps/">Our apps</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/#faq">FAQ</a></li>
          <li><a href="/privacy.html">Privacy</a></li>
          <li><a href="/terms.html">Terms</a></li>
          <li><a href="mailto:info@shoplyapps.com">info@shoplyapps.com</a></li>
        </ul>
      </div>
      <p class="fine">© 2026 Shoply Apps. Shopify is a trademark of Shopify Inc.</p>
    </div>
  </footer>
</body>
</html>
'''
HEAD_EXTRAS = '''  <link rel="alternate" type="application/rss+xml" title="Shoply Apps blog" href="https://shoplyapps.com/blog/feed.xml">
  <link rel="icon" href="/assets/favicon-96.png" sizes="96x96" type="image/png">
  <link rel="icon" href="/assets/favicon-48.png" sizes="48x48" type="image/png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
'''
page = page.replace('  <link rel="icon" href="/assets/shoply-apps-favicon.svg" type="image/svg+xml">\n', '  <link rel="icon" href="/assets/shoply-apps-favicon.svg" type="image/svg+xml">\n' + HEAD_EXTRAS, 1)
page = page.replace('<body>\n', '<body>\n  <a class="skip" href="#main">Skip to content</a>\n', 1).replace('<main>', '<main id="main">', 1)
open('blog/index.html', 'w').write(page)
print('built', len(posts))
