import sys

N = int(sys.stdin.readline().rstrip())
tag = {}

for _ in range(N):
    temp = list(map(str, sys.stdin.readline().rstrip().split(' ')))[2:]
    for element in temp:
        tag[element] = tag.get(element, 0) + 1
else:
    M = max(tag.values())
    tmp = [ k for k, v in tag.items() if M == v]
    if len(tmp) == 1 :
        print(tmp[0])
    else:
        print(-1)