#로마문자 문제 아님!

import sys

x = { 1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IIII'}

N = int(sys.stdin.readline().rstrip())
if N % 5 == 0:
    print('V' * (N // 5))
else:
    print('V' * (N // 5) + x[N % 5])