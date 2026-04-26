import sys
import re

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Nav Array
nav_match = re.search(r'const [a-zA-Z0-9]+=\[({name:"[^"]+",path:"[^"]+"},?)+\];', content)
if nav_match:
    print("NAV ARRAY:", nav_match.group(0))

# Find individual case/video titles usage
# The user wants "A Systematic Approach..." style for all headers.
# I already replaced some, but maybe not in the specific case study pages.
# Let's see some case study title text
case_titles = ["Routing and Network Optimization", "Inventory Management", "Production Scheduling"]
for title in case_titles:
    idx = content.find(title)
    if idx >= 0:
        print(f"CASE TITLE '{title}' CONTEXT:")
        print(content[idx-150:idx+150])

# Find where the case study "subtitle" is rendered
# subtitle:"Dynamic Logistics Systems"
idx_sub = content.find("Dynamic Logistics Systems")
if idx_sub >= 0:
    print("SUBTITLE CONTEXT:")
    print(content[idx_sub-150:idx_sub+150])
