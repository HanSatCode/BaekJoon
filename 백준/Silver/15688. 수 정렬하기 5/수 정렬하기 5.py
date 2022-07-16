import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n) :
    li.append(int(sys.stdin.readline()))

for x in sorted(li) :
    print(x)