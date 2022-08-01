import sys

for _ in range(int(sys.stdin.readline().strip('\n'))) :
    S1n = int(sys.stdin.readline().strip('\n'))
    S1 = set(map(int, sys.stdin.readline().strip('\n').split()))
    # S1 = sorted(set(map(int, sys.stdin.readline().strip('\n').split()))) # 중복 제거
    S2n = int(sys.stdin.readline().strip('\n'))
    S2 = list(map(int, sys.stdin.readline().strip('\n').split())) # 비교 대상
    
    for num in S2 :
        if num in S1 :
            print(1)
        else :
            print(0)

    # for S2_num in S2 :                  왜 시간초과 ? 모르겠다
    #     left = 0
    #     right = len(S1) - 1
    #     while left <= right :
    #         mid = (right + left) // 2
            
    #         if S1[mid] == S2_num :
    #             sys.stdout.write(f'1\n')
    #             break
    #         elif S1[mid] > S2_num :
    #             right = mid - 1
    #         else : # S1[mid] < S2_num
    #             left = mid + 1
    #     else :
    #         sys.stdout.write(f'0\n')