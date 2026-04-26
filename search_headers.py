import sys
import re

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find font-bold text-Xxl patterns
matches = re.findall(r'className:"[^"]*text-[3456789]xl[^"]*font-bold[^"]*"', content)
for m in set(matches):
    print(m)

matches2 = re.findall(r'className:"[^"]*font-bold[^"]*text-[3456789]xl[^"]*"', content)
for m in set(matches2):
    print(m)
