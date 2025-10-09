import sys

L = []

for _ in range(3):
    L.append(sys.stdin.readline().strip()[0])
else:
    L.sort()
    if L == ['k', 'l', 'p']:
        print("GLOBAL")
    else:
        print("PONIX")