# Build /blog/feed.xml (RSS 2.0) from the article folders
import re, html, glob, os
from email.utils import format_datetime
from datetime import datetime, timezone
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
items = []
for f in sorted(glob.glob('blog/*/index.html')):
    slug = f.split('/')[1]; s = open(f).read()
    if not os.path.exists(f'assets/blog/{slug}.jpg'): continue
    title = html.unescape(re.search(r'<h1>(.*?)</h1>', s, re.S).group(1)).strip()
    desc = html.unescape(re.search(r'<meta name="description" content="(.*?)">', s).group(1))
    date = re.search(r'"datePublished": "([\d-]+)"', s).group(1)
    items.append((date, slug, title, desc))
items.sort(key=lambda x: (x[0], x[1]), reverse=True)
e = lambda x: html.escape(x, quote=False)
pub = lambda d: format_datetime(datetime.strptime(d, '%Y-%m-%d').replace(hour=8, tzinfo=timezone.utc))
out = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">', '<channel>',
       '  <title>Shoply Apps blog</title>', '  <link>https://shoplyapps.com/blog/</link>',
       '  <atom:link href="https://shoplyapps.com/blog/feed.xml" rel="self" type="application/rss+xml"/>',
       '  <description>Practical guides for Shopify merchants on dropshipping, pricing, shipping, marketing, SEO and catalog health.</description>',
       '  <language>en</language>', f'  <lastBuildDate>{pub(items[0][0])}</lastBuildDate>']
for date, slug, title, desc in items:
    url = f'https://shoplyapps.com/blog/{slug}/'
    out += ['  <item>', f'    <title>{e(title)}</title>', f'    <link>{url}</link>', f'    <guid>{url}</guid>',
            f'    <pubDate>{pub(date)}</pubDate>', f'    <description>{e(desc)}</description>',
            f'    <enclosure url="https://shoplyapps.com/assets/blog/{slug}.jpg" type="image/jpeg" length="{os.path.getsize(f"assets/blog/{slug}.jpg")}"/>', '  </item>']
out += ['</channel>', '</rss>', '']
open('blog/feed.xml', 'w').write('\n'.join(out))
print('feed items', len(items))
