import sys
import re

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect the "Turning Data" area
idx = content.find("Turning Data")
if idx >= 0:
    print("--- TURNING DATA ---")
    print(content[idx-300:idx+400])

print("\n--- CONTACT BUTTONS ---")
# Let's find all occurrences of "Contact" that have a href or to route
for m in re.finditer(r'.{0,100}to:"/contact".{0,100}', content):
    print("FOUND CONTACT TO:")
    print(m.group(0))
