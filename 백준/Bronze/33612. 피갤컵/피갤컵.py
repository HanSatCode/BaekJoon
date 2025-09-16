import sys

N = 7 * int(sys.stdin.readline().rstrip())
print(str(2024 + N // 12) + ' ' + str(N % 12 + 1))