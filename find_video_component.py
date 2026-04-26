import sys
import re

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Usage was f.jsx(Ci, { src: "/videos/energy.mp4" })
# Component Ci definition could be something like: const Ci = (props) => ... or Ci = ({src}) => ...
# Let's search for "Ci=" followed by function start
match = re.search(r'Ci=\(\{src:([a-zA-Z0-9]+)\}\)=>.*?\"video\"', content)
if match:
    print("FOUND Ci DEFINITION:")
    print(match.group(0))

# If not found, look for more general pattern
if not match:
    # Try finding where "video" is used as a tag nearby src
    # Pattern: f.jsx("video",{src:...,...})
    for m in re.finditer(r'f.jsx\("video",\{src:[^}]+\}\)', content):
        print("FOUND VIDEO JSX DIRECTLY:")
        print(m.group(0))

# Find where Ci is assigned
idx = content.find('Ci=')
if idx >= 0:
    print("Ci= assignment area:")
    print(content[idx:idx+500])
