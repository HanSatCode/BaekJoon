import sys

M, K = map(int, sys.stdin.readline().rstrip().split(' '))

print( 'Yes' if M % K == 0 else 'No')