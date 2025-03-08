import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

study = dict()
result = 0

for x in range(N):
    cnt = int(sys.stdin.readline().rstrip())
    temp = list(sys.stdin.readline().rstrip().split(' '))
    for element in temp:
        study[element] = study.get(element, 0) + 1
else:
    for k, v in study.items():
        if v >= M:
            result += 1
    else:
        print(result)