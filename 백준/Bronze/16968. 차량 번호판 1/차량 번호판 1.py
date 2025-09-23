import sys

Q = sys.stdin.readline().strip()
R = 1

for x in range(len(Q)):
    if Q[x] == "c":
        if x > 0 and Q[x-1] == "c":
            R *= 25;
        else:
            R *= 26;
    else: # "d"
        if x > 0 and Q[x-1] == "d":
            R *= 9;
        else:
            R *= 10;
print(R)