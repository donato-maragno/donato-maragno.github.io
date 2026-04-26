import sys
import re

file_path = './assets/index-YRROGjnA.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Contact back to Nav next to About
nav_old = 'const h=[{name:"Services",path:"/"},{name:"About",path:"/about"}];'
nav_new = 'const h=[{name:"Services",path:"/"},{name:"About",path:"/about"},{name:"Contact",path:"/contact"}];'
content = content.replace(nav_old, nav_new)

# 2. Fix case study headers to have the same "mono smaller white uppercase" style
# Patterns found:
# text-4xl md:text-5xl font-bold text-white mb-6 tracking-tight
# text-3xl md:text-5xl font-bold mb-6
# text-2xl font-bold mb-4

header_replacements = {
    'text-4xl md:text-5xl font-bold text-white mb-6 tracking-tight': 'text-xl lg:text-2xl mono font-bold tracking-widest text-white mb-4 leading-tight uppercase',
    'text-3xl md:text-5xl font-bold mb-6': 'text-lg lg:text-xl mono font-bold tracking-widest text-white mb-4 leading-tight uppercase',
    'text-2xl font-bold mb-4': 'text-md lg:text-lg mono font-bold tracking-widest text-white mb-2 leading-tight uppercase',
}

for old, new in header_replacements.items():
    content = content.replace(old, new)

# 3. Privacy Policy position
# User said: "put the privacy button next to scholar or before linkedin!"
# Let's check where LinkedIn is
# f.jsx("a",{href:"https://linkedin.com/in/donato-m
linkedin_str = 'f.jsx("a",{href:"https://linkedin.com/in/donato-maragno"' # or similar
# Let's find the anchors in the footer
# In previous step I did:
# f.jsx("a",{href:"/privacy.html",target:"_blank",className:"hover:text-white transition-colors",children:"Privacy Policy"}),f.jsx("a",{href:"https://linkedin.com/in/donato-

# Let's clean up and make sure it's exactly where they want it.
# I'll search for LinkedIn and ensure Privacy Policy is before it.

# 4. Small fonts bigger (already done, but let's check text-[10px] -> text-[13px])
# I already ran change_sizes.py, so they should be already bumped.

# 5. Into Decisions color (user said: "Into Decisions. use the same style as the first part just a different color.")
# I already changed it to orange-500.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied fixes: Nav updated, Case Study headers restyled.")
