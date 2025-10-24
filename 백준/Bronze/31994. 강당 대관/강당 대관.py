import sys

name = ""
value = 0
for x in range(7):
    s, v = map(str, sys.stdin.readline().split())
    if int(v) > value:
        value = int(v)
        name = s
print(name)