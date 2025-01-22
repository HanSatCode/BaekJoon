import sys
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
if A > B:
    print(1)
elif A < B:
    print(-1)
else:
    print(0)