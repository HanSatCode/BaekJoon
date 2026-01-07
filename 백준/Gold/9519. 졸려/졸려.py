import sys

X = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

stack = []
stack.append(S)

if len(S) % 2 == 0:    # 짝수
    while True:
        left = S[0::2]
        right = S[-1:0:-2]
        S = left + right
        if S in stack:
            break
        stack.append(S)
else:                   # 홀수
    for _ in range(X):
        left = S[0::2]
        right = S[-2:0:-2]
        S = left + right
        if S in stack:
            break
        stack.append(S)
print(stack[X % len(stack)])