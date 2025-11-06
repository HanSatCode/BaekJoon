import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    t = int(sys.stdin.readline().strip())
    if (t % 25 >= 17):
        print("OFFLINE")
    else:
        print("ONLINE")