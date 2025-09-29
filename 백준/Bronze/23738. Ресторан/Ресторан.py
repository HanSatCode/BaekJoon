import sys

A = {'B' : 'v', 'E' : "ye", 'H' : 'n', 'P' : 'r', 'C' : 's', 'Y' : 'u', 'X' : 'h'}
R = ""

for x in sys.stdin.readline().strip():
    R += A.get(x, x.lower())
print(R)