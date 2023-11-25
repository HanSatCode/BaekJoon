import sys

N = int(sys.stdin.readline().strip())
R = 0
'''
1~9 -> 1 * 9
10~99 -> 2 * 90
100~999 -> 3 * 900
1000~9999 -> 4 * 9000
...
'''
if N < 10:    # 1의 자리
    print(N)
else:
    for x in range(1, len(str(N))):
        R += x * int(str(9) + (str(0) * (x - 1)))
    R += len(str(N)) * int(N - int(str(9) * int(len(str(N))-1)))
    print(R)