import sys

N = int(sys.stdin.readline().rstrip())
R = 0

for x in range(1, N + 1):
    temp = str(x)
    R += temp.count('3') + temp.count('6') + temp.count('9')
else:
    print(R)