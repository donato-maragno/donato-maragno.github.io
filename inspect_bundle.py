import sys

with open('./assets/index-YRROGjnA.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("zw=()=>")
if idx >= 0:
    print("Found zw (Footer):")
    print(content[idx:idx+800])

print("\n---")
idx2 = content.find("Supply Chain Optimization")
if idx2 >= 0:
    print("Found Supply Chain Optimization:")
    print(content[idx2-200:idx2+150])

print("\n---")
idx3 = content.find("Problem Definition")
if idx3 >= 0:
    print("Found Problem Definition:")
    print(content[idx3-200:idx3+100])
