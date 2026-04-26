import sys
import re

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find "Scholar" or "LinkedIn"
idx2 = content.find('children:"LinkedIn"')
if idx2 >= 0:
    print(content[idx2-200:idx2+200])

idx3 = content.find('children:"Scholar"')
if idx3 >= 0:
    print(content[idx3-200:idx3+200])
