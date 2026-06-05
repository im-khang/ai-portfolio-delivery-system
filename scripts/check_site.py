#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import re

ROOT = Path(__file__).resolve().parents[1]
html_path = ROOT / 'src' / 'index.html'
css_path = ROOT / 'src' / 'styles.css'
html = html_path.read_text(encoding='utf-8')
css = css_path.read_text(encoding='utf-8')

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.headings = []
        self.tables = 0
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'a':
            self.links.append(d.get('href', ''))
        if tag in {'h1','h2','h3'}:
            self.headings.append(tag)
        if tag == 'table':
            self.tables += 1

parser = LinkParser()
parser.feed(html)
checks = {
    'has_title': '<title>Khang Nguyen — Agentic Developer</title>' in html,
    'has_h1': 'Hi, I’m Khang' in html,
    'has_claim_boundary': 'Claim boundary' in html,
    'has_maturity_table': parser.tables == 1,
    'has_contact': 'khangdnguyen.work@gmail.com' in html and '+84' in html,
    'has_no_empty_case_placeholder': 'coming soon' not in html.lower(),
    'has_mobile_media_query': '@media (max-width: 820px)' in css,
    'has_responsive_grid': 'grid-template-columns: repeat(3, 1fr)' in css,
    'all_links_have_href': all(bool(x) for x in parser.links),
}
failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(f'{name}: {ok}')
if failed:
    raise SystemExit('FAILED: ' + ', '.join(failed))
print('PASS')
