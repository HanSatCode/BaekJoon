import sys

T = int(sys.stdin.readline().rstrip())

for x in range(T):
    tmp = sys.stdin.readline().rstrip()
    r = int(tmp) + int (tmp[::-1])
    print("YES" if str(r) == str(r)[::-1] else "NO")