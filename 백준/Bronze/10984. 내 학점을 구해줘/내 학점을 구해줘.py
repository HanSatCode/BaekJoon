T = int(input())
for _ in range(T):
    N = int(input())
    GS = 0
    GP = 0
    for x in range(N):
        temp1, temp2= map(float, input().split(' '))
        GS += temp1 * temp2
        GP += temp1
    print(f"{int(GP)} {GS/GP:.1f}")    