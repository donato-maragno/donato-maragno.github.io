import sys

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("zw=()=>")
if idx >= 0:
    print("FOOTER:")
    print(content[idx:idx+1500])
