import sys

pri1 =  [500, 300, 200, 50, 30, 10]
per1 = [1, 3, 6, 10, 15, 21]
pri2 = [512, 256, 128, 64, 32]
per2 = [1, 3, 7, 15, 31]

T = int(sys.stdin.readline().rstrip())
a, b, ra, rb = 0, 0, 0, 0
for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    ra = 0
    rb = 0
    for x in range(6):
        if a == 0 or a > per1[-1]:
            break
        if a <= per1[x] and ra < pri1[x]:
            ra = pri1[x]
    for x in range(5):
        if b == 0 or b > per2[-1]:
            break
        if b <= per2[x] and rb < pri2[x]:
            rb = pri2[x]
    if ra + rb == 0:
        print('0')
    else:
        print(str(ra + rb) + "0000")