import sys

k = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
origin = [ chr(x) for x in range(65, 65+k) ]
answer = list(sys.stdin.readline().strip())
line = []
checker = 0
R = []


for x in range(n):
    T = list(sys.stdin.readline().strip())
    if T[0] == '?':
        checkPoint = x
        break
    if not checker: # 물음표 전 구간(origin 변경 구간)
        for x in range(k - 1):
            if T[x] == '-': # 스위치
                origin[x], origin[x + 1] = origin[x + 1], origin[x]

for x in range(checkPoint + 1, n):
    line.append(list(sys.stdin.readline().strip()))

for x in range(len(line) - 1, -1, -1):
    for y in range(k - 1):
        if line[x][y] == '-': # 스위치
            answer[y], answer[y + 1] = answer[y + 1], answer[y]

for x in range(k - 1):
    if origin[x] != answer[x]: 
        origin[x], origin[x + 1] = origin[x + 1], origin[x]
        R.append('-')
    else: R.append('*')
    
if origin != answer: print('x' * (k - 1))
else: print(''.join(R))