import sys

right = int(sys.stdin.readline())
left = 1
R = right

while left <= right :
    mid = (right + left) // 2
    #print(left, right, mid)
    if mid ** 2 == R :
        print(mid)
        break
    elif mid**2 > R :
        right = mid - 1
    elif mid**2 < R :
        left = mid + 1