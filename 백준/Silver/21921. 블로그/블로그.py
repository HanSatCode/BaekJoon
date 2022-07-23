import sys

days, c = map(int, sys.stdin.readline().split())
come = list(map(int, sys.stdin.readline().split()))

cDat, mDat, mCnt = 0, 0, 0

for x in range(days-c+1) :
    if x == 0 :
        cDat = sum(come[x:x+c])
        mCnt = 1
        mDat = cDat
    else :
        cDat = cDat - come[x-1] + come[x+c-1]
        if cDat >= mDat :
            if cDat != mDat :
                mCnt = 1
            else :
                mCnt += 1
            mDat = cDat
else :
    if mDat == 0 :
        print('SAD')
    else :
        print(f'{mDat}\n{mCnt}')