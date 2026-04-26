import sys
import re

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

print("--- EXAMINING LABELS ---")
for m in re.finditer(r'className:"[^"]*mono[^"]*text-\[[0-9]+px\][^"]*"', content):
    print(m.group(0))

for m in re.finditer(r'className:"[^"]*text-\[[0-9]+px\][^"]*mono[^"]*"', content):
    print(m.group(0))
