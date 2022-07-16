import sys

N, M = map(int, sys.stdin.readline().split())

dicNum = {}
dicName = {}

for x in range(1, N+1) :
    temp = sys.stdin.readline().strip('\n')
    dicNum[x] = temp
    dicName[temp] = x

for _ in range(M) :
    q = sys.stdin.readline().strip('\n')
    if q.isdigit() : # 숫자를 받았을 때
        print(dicNum[int(q)])
    else : # 문자를 받았을 때
        print(dicName[q])