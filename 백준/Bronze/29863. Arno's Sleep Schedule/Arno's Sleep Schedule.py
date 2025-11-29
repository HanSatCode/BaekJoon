import sys

H = int(sys.stdin.readline().rstrip())
W = int(sys.stdin.readline().rstrip())

if (20 <= H <= 23) :
    print((24 - H) + W)
else:
    print(W - H)