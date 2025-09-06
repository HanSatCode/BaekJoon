import sys

n = 0
for _ in range(4) :
    n += int(sys.stdin.readline().strip())
else:
    if (n <= 1500) :
        print("Yes")
    else :
        print("No")