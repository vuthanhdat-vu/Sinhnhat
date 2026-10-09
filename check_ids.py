import re

with open('index.html', 'r', encoding='utf-8') as f:
    code = f.read()

ids_in_html = set(re.findall(r'id=["\']([^"\']+)["\']', code))
ids_in_js = set(re.findall(r'getElementById\(["\']([^"\']+)["\']\)', code))
print('HTML IDs count:', len(ids_in_html))
print('JS IDs count:', len(ids_in_js))
print('Missing in HTML:', ids_in_js - ids_in_html)
  