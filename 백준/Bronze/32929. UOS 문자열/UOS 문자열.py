import sys

x = int(sys.stdin.readline().rstrip())

if x % 3 == 0:
    print("S")
elif x % 3 == 1:
    print("U")
else:
    print("O")