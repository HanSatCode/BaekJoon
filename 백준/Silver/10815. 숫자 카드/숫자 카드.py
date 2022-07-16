_ = int(input())
N = sorted(list(map(int, input().split())))
_ = int(input())
M = list(map(int, input().split())) # Result

for num in M :
    left = 0
    right = len(N) - 1
    while left <= right :
        mid = (left + right) // 2
        if N[mid] == num :
            print('1', end=' ')
            break
        elif N[mid] > num :
            right = mid - 1
        else :
            left = mid + 1
    else :
        print('0', end=' ')