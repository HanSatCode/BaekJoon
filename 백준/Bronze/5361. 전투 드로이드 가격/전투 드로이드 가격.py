import sys

T = int(sys.stdin.readline().rstrip())
for x in range(T):
    AE = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    PER = [350.34, 230.90, 190.55, 125.30, 180.90]
    answer = 0
    for y in range(5):
        answer += AE[y] * PER[y]
    print(f"${answer:.2f}")