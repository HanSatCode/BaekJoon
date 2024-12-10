import sys

T = int(sys.stdin.readline().rstrip())
P = []
for x in range(T):
    P.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

for x in range(T):
    rank = 1
    for y in range(T):
        if P[x][0] < P[y][0] and P[x][1] < P[y][1]: #본인이 몸무게 및 키 둘다 작을 때
            rank += 1
    print(rank, end = " ")