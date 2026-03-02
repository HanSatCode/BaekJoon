A = list(map(int, input().split()))
while A != [1, 2, 3, 4, 5]:
    for x in range(4):
        if A[x] > A[x + 1]:
            A[x], A[x + 1] = A[x + 1], A[x]
            print(*A)