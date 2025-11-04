import sys

N = int(sys.stdin.readline().strip())
M = -1
Mt = -1
C = {0 : "PROBRAIN", 1 : "GROW", 2 : "ARGOS",
     3 : "ADMIN", 4 : "ANT", 5 : "MOTION",
     6 : "SPG", 7 : "COMON", 8 : "ALMIGHTY"}

for x in range(9):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for element in temp:
        if M < element:
            M = element
            Mt = x
else:
    print(C[Mt])