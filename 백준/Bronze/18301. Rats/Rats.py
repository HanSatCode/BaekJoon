import sys
A, B, C = map(int, sys.stdin.readline().rstrip().split(' '))
print(int((A+1)*(B+1)/(C+1) - 1))