T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    L = []
    R = 0
    for y in range(m):
        L.append(list(map(int, input().split())))
    for x in range(n):
        yL = [ L[y][x] for y in range(m)]
        cnt = 0
        pIndex = m -1
        for idx in range(m - 1, -1, -1):
            if yL[idx] == 1: 
                R += pIndex - idx
                pIndex -= 1
    print(R)