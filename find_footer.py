import sys
import re

fname = './assets/index-YRROGjnA.js'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all 'children:"Scholar"'
for m in re.finditer(r'children:"Scholar"', content):
    print(f"SCHOLAR AT {m.start()}:")
    print(content[m.start()-250:m.start()+150])

print("\n---")
# Find all 'children:"LinkedIn"'
for m in re.finditer(r'children:"LinkedIn"', content):
    print(f"LINKEDIN AT {m.start()}:")
    print(content[m.start()-250:m.start()+150])
