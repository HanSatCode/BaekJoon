import sys

H, M = map(int, sys.stdin.readline().split())
newM = int(sys.stdin.readline().strip())

totalM = H * 60 + M + newM
newH = (totalM // 60 % 24)
newM = totalM % 60
print(newH, newM)