import sys
import re

fname = './assets/index-YRROGjnA.js'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()

header_map = {
    'className:"text-2xl md:text-4xl text-white font-bold tracking-tight leading-tight"': 'className:"text-lg lg:text-xl mono font-bold tracking-widest text-white uppercase leading-tight"',
    'className:"text-3xl md:text-4xl font-bold mb-12 border-b border-[#ea580c]/30 pb-6"': 'className:"text-xl lg:text-2xl mono font-bold tracking-widest text-white mb-8 border-b border-[#ea580c]/30 pb-4 uppercase"',
    'className:"text-5xl md:text-7xl font-bold tracking-tighter mb-6"': 'className:"text-3xl lg:text-5xl mono font-bold tracking-widest text-white mb-6 uppercase leading-tight"',
    'className:"text-3xl md:text-5xl font-bold tracking-tight mb-8 leading-tight"': 'className:"text-lg lg:text-xl mono font-bold tracking-widest text-white mb-6 uppercase leading-tight"',
}

for old, new in header_map.items():
    content = content.replace(old, new)

with open(fname, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final header cleanup done.")
