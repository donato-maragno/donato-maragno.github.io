import sys
import re

fname = './assets/index-YRROGjnA.js'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Contact button in Nav
nav_old = 'const h=[{name:"Services",path:"/"},{name:"About",path:"/about"}];'
nav_new = 'const h=[{name:"Services",path:"/"},{name:"About",path:"/about"},{name:"Contact",path:"/contact"}];'
if nav_old in content:
    content = content.replace(nav_old, nav_new)
    print("Added Contact back to Nav.")

# 2. Privacy Policy in Global Footer
# Let's find the footer items. Usually they are like:
# f.jsx("a",{href:"...",children:"LinkedIn"}),f.jsx("a",{href:"...",children:"GitHub"}),f.jsx("a",{href:"...",children:"Scholar"})
# I'll look for Scholar and put Privacy before/next to it.

scholar_match = re.search(r'f\.jsx\("a",\{href:"https://scholar\.google\.com/[^"]+",target:"_blank",rel:"noopener",className:"hover:text-white transition-colors",children:"Scholar"\}\)', content)
if scholar_match:
    privacy_btn = 'f.jsx("a",{href:"/privacy.html",className:"hover:text-white transition-colors",children:"Privacy Policy"}),'
    if 'children:"Privacy Policy"' not in scholar_match.group(0): # Avoid duplicates
        content = content.replace(scholar_match.group(0), privacy_btn + scholar_match.group(0))
        print("Added Privacy Policy to global footer.")

# 3. Case study headers consistency
# I already did some, but let's make sure ALL headers in video pages are fixed.
# Nw, ww, etc. components.
sections = ['Strategic Vision', 'The Optimization Framework', 'The Problem', 'The Solution', 'Impact Across Sectors']
for section in sections:
    # Find h2 or similar with these titles
    # Pattern: f.jsx("h2",{className:"...",children:"TITLE"})
    match = re.search(r'f\.jsx\("h2",\{className:"([^"]*)",children:"' + re.escape(section) + '"\}', content)
    if match:
        old_classes = match.group(1)
        # Systematic style: text-xl lg:text-2xl mono font-bold tracking-widest text-white mb-4 leading-tight uppercase
        new_classes = 'text-xl lg:text-2xl mono font-bold tracking-widest text-white mb-4 leading-tight uppercase'
        content = content.replace(f'className:"{old_classes}",children:"{section}"', f'className:"{new_classes}",children:"{section}"')
        print(f"Updated header '{section}' style.")

# 4. Small fonts bigger (Labels like "Phase 01", "Dynamic Logistics Systems")
# These usually have `text-[10px]` or similar.
# I already bumped them in change_sizes.py but I'll do a check for `text-[11px]` and similar if they need more.
# User asked "a bit bigger". 10px -> 13px is a good jump. 11px -> 14px.
# Let's check for `text-xs` which is 12px. Bump to `text-sm`.
content = content.replace('text-xs', 'text-sm')

with open(fname, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final UI adjustments applied.")
