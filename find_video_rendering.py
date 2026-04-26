import sys
import re

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for patterns where "video" might be used as a tag in f.jsx or f.jsxs
# Often looks like: f.jsx("video",{...})
for m in re.finditer(r'f.js[xs]*\("video",\{[^\}]+\}\)', content):
    print("FOUND VIDEO JSX:")
    print(m.group(0))

# Also search for <video instances if it's template literal (unlikely in this minified build but check)
for m in re.finditer(r'<video[^>]*>', content):
    print("FOUND HTML VIDEO TAG:")
    print(m.group(0))

# Search for where videoSrc is used
for m in re.finditer(r'src:[a-zA-Z0-9]+\.videoSrc', content):
    print("FOUND SRC USE OF videoSrc:")
    print(content[m.start()-100:m.end()+100])
