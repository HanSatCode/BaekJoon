import sys

result = []

def backTracking(list):
    if len(list) == N :
        print(''.join(map(str, list)))
        sys.exit()
    else:
        for x in range(1, 4): # 1, 2, 3
            list.append(x)
            if len(list) >= 2:
                #생각해보니까 앞에서 검사했으면 뒤에만 검사하면 될듯하다
                mid = len(list) // 2
                for x in range(1, mid + 1):
                    if list[-x:] == list[-(2*x):-x]:
                        break
                else:
                    backTracking(list)
            else: # len(list) == 1:
                backTracking(list)
            list.pop()


N = int(sys.stdin.readline().rstrip())
backTracking([])