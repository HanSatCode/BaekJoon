import sys

Ax, Ay = map(int, sys.stdin.readline().split())
Bx, By = map(int, sys.stdin.readline().split())
Cx, Cy = map(int, sys.stdin.readline().split())

judge = ((Bx - Ax) * (Cy - Ay)) - ((Cx - Ax) * (By - Ay))

print(-1 if judge < 0 else 1 if judge > 0 else 0)