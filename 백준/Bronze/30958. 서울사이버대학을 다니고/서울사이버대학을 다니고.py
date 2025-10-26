import sys

N = int(sys.stdin.readline().strip())
L = list(sys.stdin.readline().strip())
E = {' ', ',', '.'}
D = {}

for element in L:
    if element in E:
        continue
    D[element] = D.get(element, 0) + 1
else:
    max_key = max(D, key=D.get)
    print(D[max_key])