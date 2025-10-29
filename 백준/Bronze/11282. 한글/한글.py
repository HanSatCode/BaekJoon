import sys
N = int(sys.stdin.readline().strip())
print(chr(N + 0xAC00 - 1))