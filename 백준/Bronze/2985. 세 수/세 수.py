import sys

A, B, C = map(int, sys.stdin.readline().strip().split(' '))

if A + B == C: print(f"{A}+{B}={C}")
elif A - B == C: print(f"{A}-{B}={C}")
elif A / B == C: print(f"{A}/{B}={C}")
elif A * B == C: print(f"{A}*{B}={C}")
elif A == B + C: print(f"{A}={B}+{C}")
elif A == B - C: print(f"{A}={B}-{C}")
elif A == B * C: print(f"{A}={B}*{C}")
else: print(f"{A}={B}/{C}")