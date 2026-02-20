import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
F = {}

stack = []
for element in A: F[element] = F.get(element, 0) + 1

answer = []
for element in A[::-1]:
    while stack and F[stack[-1]] <= F[element]:
        stack.pop()

    if not stack: answer.append(-1)
    else: answer.append(stack[-1])

    stack.append(element)

print(*answer[::-1])