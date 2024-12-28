import sys

N = int(sys.stdin.readline().rstrip())
answer = 0

for x in range(1, N + 1):
    answer += x
else:
    print(f"{answer}\n{answer ** 2}\n{answer ** 2}")