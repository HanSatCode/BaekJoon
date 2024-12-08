import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split(" "))
R = 1

if B == 1:
    print(A % C)
else:
    while B > 0:
        if B % 2 != 0:
            R *= A % C 
            B -= 1
        A *= A % C
        B //= 2
    else:
        print(R % C)