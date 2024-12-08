import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split(' '))

if V < A:
    print(1);
else:
    temp = (V - B) / (A - B)
    if temp == int(temp):
        print(int(temp))
    else:
        print(int(temp) + 1)