import sys

a = []
for _ in range(5):
    a.append(int(sys.stdin.readline().rstrip()))
else:
    print(sum([min(a[:3]), min(a[3:]), - 50]))