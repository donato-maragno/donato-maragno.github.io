import sys

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the micro text classes slightly larger
content = content.replace('text-[11px]', 'text-[14px]')
content = content.replace('text-[10px]', 'text-[13px]')
content = content.replace('text-[9px]', 'text-[12px]')
content = content.replace('text-[8px]', 'text-[11px]')

# Also there was an explicit text-xs for Phase which is 12px natively
# className:"text-xs font-bold uppercase tracking-widest",children:g[x+1].title
# The user said Phase 01... and all the ones with the same font size a bit bigger
# We can bump text-xs up to text-sm in those Phase blocks? Yes, let's bump `text-xs` to `text-sm` generally when it's mono
content = content.replace('text-xs', 'text-sm')

with open('./assets/index-YRROGjnA.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied font size bump to UI micro-labels.")
