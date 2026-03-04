import sys
import math

N, Q = map(int, sys.stdin.readline().strip().split(' '))
X = list(map(int, sys.stdin.readline().strip().split(' ')))
Y = list(map(int, sys.stdin.readline().strip().split(' ')))

prefix_sum_left = [0.0] * (N + 1)
prefix_sum_right = [0.0] * (N + 1)
drain = 0

for index in range(1, N):
    dx = X[index] - X[index - 1]
    dy = Y[index] - Y[index - 1]
    drain = math.hypot(dx, dy)
    if dy == 0: drain = dx * 2 # 평지
    elif dy > 0 : drain *= 3 # 오르막길
    prefix_sum_left[index + 1] = drain + prefix_sum_left[index]

for index in range(N - 1, 0, -1): # right to left
    dx = X[index] - X[index - 1]
    dy = Y[index] - Y[index - 1]
    drain = math.hypot(dx, dy)
    if dy == 0: drain = dx * 2 # 평면
    elif dy < 0: drain *= 3 # 오르막길
    prefix_sum_right[index] = drain + prefix_sum_right[index + 1]

for _ in range(Q):
    start, end = map(int, sys.stdin.readline().strip().split(' '))
    if start < end:
        print(prefix_sum_left[end] - prefix_sum_left[start])
    else: # 우 -> 좌
        print(prefix_sum_right[end] - prefix_sum_right[start])