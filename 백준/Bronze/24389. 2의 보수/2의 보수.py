import sys

N = int(sys.stdin.readline().strip())
NA = (N ^ ((1 << 32) - 1)) + 1
print((N ^ NA). bit_count())