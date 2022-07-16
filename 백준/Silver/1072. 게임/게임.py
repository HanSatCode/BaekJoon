x, y = map(int, input().split())
z = y*100//x
mini= 0
maxi = 1000000000
medi = 0

if z >= 99 :
    print("-1")
else :
    while mini <= maxi :
        medi = (mini + maxi)//2
        rX = x + medi
        rY = y + medi
        if rY*100//rX > z :
            maxi = medi - 1
        else :
            mini = medi + 1
    print(maxi+1)