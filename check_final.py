import sys

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

print("--- FOOTER ITEMS ---")
# Check if "Privacy Policy" is in the footer
idx1 = content.find('children:"Privacy Policy"')
print("Found 'Privacy Policy' at:", idx1)
if idx1 >= 0:
    print(content[idx1-200:idx1+150])

print("--- STAGE ITEMS ---")
# Check video dimensions
idx2 = content.find('className:"stage-item flex-shrink-0')
if idx2 >= 0:
    print(content[idx2:idx2+200])

