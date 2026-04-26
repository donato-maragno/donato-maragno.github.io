import sys
import re

fname = './assets/index-YRROGjnA.js'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Section headers / Smaller big headers
header_map = {
    'className:"text-4xl md:text-5xl font-bold mb-16 text-center tracking-tight"': 'className:"text-xl lg:text-2xl mono font-bold tracking-widest text-white mb-8 text-center uppercase"',
    'className:"text-3xl md:text-4xl font-bold mb-8"': 'className:"text-lg lg:text-xl mono font-bold tracking-widest text-white mb-4 uppercase"',
    'className:"text-4xl md:text-6xl font-bold tracking-tighter"': 'className:"text-2xl lg:text-3xl mono font-bold tracking-widest text-white mb-6 uppercase"',
    'className:"text-5xl md:text-8xl font-bold tracking-tighter mb-6"': 'className:"text-3xl lg:text-5xl mono font-bold tracking-widest text-white mb-6 uppercase leading-tight"',
    'className:"text-4xl lg:text-5xl font-bold text-white tracking-tighter mb-6"': 'className:"text-xl lg:text-2xl mono font-bold tracking-widest text-white mb-6 uppercase"',
    'className:"text-3xl md:text-5xl font-bold tracking-tight mb-6"': 'className:"text-lg lg:text-xl mono font-bold tracking-widest text-white mb-6 uppercase"',
    'className:"text-4xl md:text-5xl font-bold text-white"': 'className:"text-xl lg:text-2xl mono font-bold tracking-widest text-white uppercase"',
    'className:"text-3xl font-bold mb-6 text-amber-500"': 'className:"text-lg lg:text-xl mono font-bold tracking-widest text-amber-500 mb-6 uppercase"',
}

for old, new in header_map.items():
    content = content.replace(old, new)

# 2. Fix the font size bump for small labels again (to be sure)
# I want them "A bit bigger". 10px -> 13px, 11px -> 14px etc.
# Already done but let's confirm the replacements.
# text-[10px] -> text-[13px]
# text-[11px] -> text-[14px]
# text-[8px] -> text-[11px]
# text-[9px] -> text-[12px]

# 3. Add Privacy Policy next to Scholar or before LinkedIn in Global Footer
# I'll check if I already added it in the previous step.

if 'children:"Privacy Policy"' not in content:
    # Find Scholar component
    scholar_str = 'children:"Scholar"}'
    privacy_btn = '{icon:KN,label:"Legal",val:"Privacy Policy",href:"/privacy.html"}' # This was for contact page
    
    # Global Footer anchors:
    # f.jsx("a",{href:"https://linkedin.com/in/donato-maragno",target:"_blank",rel:"noopener",className:"hover:text-white transition-colors",children:"LinkedIn"})
    linkedin_anchor = 'f.jsx("a",{href:"https://linkedin.com/in/donato-maragno",target:"_blank",rel:"noopener",className:"hover:text-white transition-colors",children:"LinkedIn"})'
    privacy_anchor = 'f.jsx("a",{href:"/privacy.html",className:"hover:text-white transition-colors",children:"Privacy Policy"}),'
    
    if linkedin_anchor in content:
        content = content.replace(linkedin_anchor, privacy_anchor + linkedin_anchor)
        print("Inserted Privacy Policy anchor in footer.")

with open(fname, 'w', encoding='utf-8') as f:
    f.write(content)

print("Headers and footer adjustments applied.")
