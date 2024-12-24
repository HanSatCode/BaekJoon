import sys

def backTracking(list):
    if len(list) == N:
        print(''.join(map(str, list)))
    else:
        for x in range(1, 10):
            # 리스트가 비어있을경우 건너뛰기 (1은 소수가 아니기 때문)
            if (not list) and (x == 1): 
               continue
            else:
                list.append(x)
                temp_cnt = 0
                current_num = int(''.join(map(str, list)))
                for y in range(2, int(current_num ** (1 / 2)) + 1):
                    if current_num % y == 0:
                        temp_cnt += 1
                else:
                    if temp_cnt == 0:
                        backTracking(list)
                list.pop()

N = int(sys.stdin.readline().rstrip())

backTracking([])