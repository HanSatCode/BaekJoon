T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    t = M * 2 - N
    print(t, M - t)