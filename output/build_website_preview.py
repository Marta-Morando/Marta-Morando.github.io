from pathlib import Path
import base64
import mimetypes
import re
from html.parser import HTMLParser

root = Path(__file__).resolve().parents[1]
source = (root / 'index.html').read_text(encoding='utf-8')
css = re.search(r'<style>(.*?)</style>', source, re.S).group(1)
css = re.sub(r'(?<![\w-])(:root|html|body)(?=\s*\{)', '#website-preview', css)
body = source.rsplit('<body>', 1)[1].split('</body>', 1)[0]
body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
assert 'The Cost of Identity' in body
assert 'abstract-text-2' not in body
assert 'button-icon-2' not in body
assert 'How do private and social identities' not in body

def embed_image(match):
    path = root / match.group(1)
    mime = mimetypes.guess_type(path)[0]
    return 'src="data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode() + '"'

body = re.sub(r'src="(pictures/[^"]+)"', embed_image, body)
body = re.sub(r'href="((?:papers|slides|cv)/[^"]+)"', r'href="https://martamorando.com/\1"', body)
toggle = source.split('<script>', 1)[1].split('function copyBibTeX', 1)[0]
script = toggle + '''
function copyBibTeX() {
    const root = document.getElementById('website-preview');
    const existing = root.querySelector('.preview-citation');
    if (existing) { existing.remove(); return; }
    const citation = document.createElement('pre');
    citation.className = 'preview-citation';
    citation.style.whiteSpace = 'pre-wrap';
    citation.textContent = 'Dossi, Gaia and Morando, Marta (2026). Polarized Technologies. CEP Discussion Paper 2116.';
    root.querySelector('#abstract-text-1').after(citation);
}
'''
fragment = '<div id="website-preview">\n<style>\n' + css + '\n#website-preview .profile { position: static; }\n</style>\n' + body + '\n</div>\n<script>\n' + script + '\n</script>\n'
out = root / 'output' / 'website-preview.html'
out.write_text(fragment, encoding='utf-8')
assert out.stat().st_size < 1_000_000
check = out.read_text(encoding='utf-8')
assert '\\"' not in check and '\\n' not in check
HTMLParser().feed(check)
print(f'Preview written and checked: {out} ({out.stat().st_size:,} bytes)')
