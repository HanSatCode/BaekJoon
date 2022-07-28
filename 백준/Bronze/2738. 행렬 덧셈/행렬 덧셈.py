N, M = map(int, input().split())
A = []
B = []
for _ in range(N) :
    A.append(list(map(int, input().split())))
for _ in range(N) :
    B.append(list(map(int, input().split())))

C = [[ A[y][x] + B[y][x] for x in range(M)] for y in range(N)]

for x in range(N) :
    for y in range(M) :
        print(C[x][y], end=' ')
    print()