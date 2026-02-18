import sys

S = list(sys.stdin.readline().strip())
one = len(set(S))
palindrome = S == S[::-1]

if one == 1: print(-1) # 문자 종류 단 하나
elif palindrome: print(len(S) - 1)
else: print(len(S))