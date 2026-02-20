import sys

N = int(sys.stdin.readline().strip())
stack = []
for x in range(N):
    temp = int(sys.stdin.readline().strip())
    while stack and stack[-1] <= temp: stack.pop()
    stack.append(temp)
print(len(stack))