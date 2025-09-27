import sys

n = int (sys.stdin.readline().strip())
C = sorted(list(map(int, sys.stdin.readline().strip().split())))
print(sum(C[:-1])) # 마지막 카드는 절대 뽑을 수 없음