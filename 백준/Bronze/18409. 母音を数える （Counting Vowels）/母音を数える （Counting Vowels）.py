import sys

check = [ 'a' , 'i', 'u', 'e', 'o' ]

a = sys.stdin.readline().rstrip()
S = sys.stdin.readline().rstrip()
R = 0

for word in S:
    if word in check:
        R += 1
else:
    print(R)