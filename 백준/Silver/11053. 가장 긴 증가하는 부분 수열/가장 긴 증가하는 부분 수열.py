import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split(' ')))

#1초인데 O(n^2) 통과가능?

result = [ 1 for x in range(N)]

for x in range(1, N):   #처음부터 탐색(암만 짧아도 1이기에 index 1부터)
    for y in range(x):  #바로 앞까지 이전 기록 참고
        if A[x] > A[y]: #크면?
            result[x]= max(result[x], result[y] + 1) #이전 기록 참고하여 기록갱신
else:
    print(max(result)) #최장 기록