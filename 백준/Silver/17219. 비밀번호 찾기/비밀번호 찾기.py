import sys

N, M = map(int, sys.stdin.readline().split())

dic = {}

for x in range(N) :
    S, P = sys.stdin.readline().split()
    dic[S] = P
for _ in range(M) :
    temp = sys.stdin.readline().strip('\n')
    print(dic[temp])