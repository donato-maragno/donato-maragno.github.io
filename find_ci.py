import sys
import re

fname = './assets/index-YRROGjnA.js'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()

# I saw f.jsx(Ci, { src: "/videos/energy.mp4" })
# Let's find Ci
m = re.search(r'([a-zA-Z0-9]+)\s*=\s*.*?\{src:([a-zA-Z0-9]+)\}', content)
# This is too broad. Let's look for components nearby
for m in re.finditer(r'([a-zA-Z0-9]+)=\(\{src:([a-zA-Z0-9]+)\}\)=>', content):
    name = m.group(1)
    body_start = m.end()
    # Find the next few f.jsx calls
    body = content[body_start:body_start+500]
    if 'video' in body:
        print(f"FOUND VIDEO COMPONENT: {name}")
        print(content[m.start():body_start+500])

# Also check for Ci specifically
m_ci = re.search(r'Ci\s*=\s*', content)
if m_ci:
    print("Ci assignment found:")
    print(content[m_ci.start():m_ci.start()+200])
