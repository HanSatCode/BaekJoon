import sys

S1, S2 = map(int, sys.stdin.readline().split())
if(S1 / S2) >= 0.5:
    print("E")
else:
    print("H")