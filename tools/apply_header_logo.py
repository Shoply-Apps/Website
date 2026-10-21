# Writes the current animated logo (tools/logo_svg.py) into the header of every page.
# Run after changing the logo: python3 tools/apply_header_logo.py
import glob, os, re, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, 'tools')
from logo_svg import SVG
pages = ['index.html', '404.html', 'apps/index.html', 'blog/index.html'] + glob.glob('blog/*/index.html')
n = 0
for f in pages:
    s = open(f).read()
    s2 = re.sub(r'<svg class="logo-mark".*?</svg><script>/\* reduced motion.*?</script>', lambda m: SVG, s, count=1, flags=re.S)
    if s2 != s: open(f, 'w').write(s2); n += 1
# the standalone animated file mirrors the inline logo (without the script)
open('assets/shoply-apps-logo-animated.svg', 'w').write(
    SVG.split('<script>')[0].replace('<svg class="logo-mark" viewBox', '<svg xmlns="http://www.w3.org/2000/svg" viewBox', 1) + '\n')
print('pages updated', n)
