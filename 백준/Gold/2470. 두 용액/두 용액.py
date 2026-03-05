import sys

N = int(sys.stdin.readline().strip())
P = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))
R = []
m = 2000000000

leftIndex = 0
rightIndex = N - 1

while leftIndex < rightIndex:
    tempSum = P[leftIndex] + P[rightIndex]
    if abs(tempSum) < m:
        m = abs(tempSum)
        R = [ P[leftIndex], P[rightIndex] ]

    # 목표 : 0에 더 가까워지도록 하기
    if tempSum < 0: 
        leftIndex += 1
    else: #tempSum > 0:
        rightIndex -= 1

print(*R, sep=" ")