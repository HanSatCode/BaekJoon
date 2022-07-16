import sys

N = int(sys.stdin.readline().strip('\n'))
R = 0

while N >= 0 :
    if N % 5 == 0 :
        R += N//5
        print(R)
        break
    else :
        N -= 3
        R += 1
else :
    print('-1')