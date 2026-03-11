import sys

direct = ["N", "E", "S", "W"]
index = 0

for _ in range(10):
    t = int(input())
    if t == 1: index += 1
    elif t == 2: index += 2
    else: index -= 1 # t == 3
    index = index % 4 # 0 ~ 3
print(direct[index])