import sys

N, X = map(int, sys.stdin.readline().split())
L = [] # 가성비있게 담자
R = 0
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
L.sort(key = lambda x: x[0] - x[1], reverse=True)

for x in range(N):
    # 가성비가 좋고, 5000원으로 사먹으면 다른 날 감당이 가능한가? (식정리)
    if L[x][0] - L[x][1] > 0 and X - 5000 >= 1000 * (N - x - 1):
        R += L[x][0]
        X -= 5000
    else:
        R += L[x][1]
        X -= 1000
print(R)