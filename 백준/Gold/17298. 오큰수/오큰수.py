import sys
from collections import deque


N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
stack = deque()
answer = []

for element in A[::-1]:
    if not stack:
        answer.append(-1)
    else:
        while stack and stack[-1] <= element: stack.pop()
        if not stack: answer.append(-1)
        else: answer.append(stack[-1])
    stack.append(element)

print(*answer[::-1])