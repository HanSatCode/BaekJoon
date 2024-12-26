import sys

def backTracking(list):
    if list and int(''.join(map(str, list))) >= 10**10:
        return
    else:
        for x in range(0, 10):
            if len(list) == 0 and x == 0:
                continue
            list.append(x)
            #print(list)
            if len(list) >= 2:
                if list[-2] > list[-1]:
                    result.append(int(''.join(map(str, list))))
                    backTracking(list)
            else: # list 길이가 1일경우
                result.append(x)
                backTracking(list)
            list.pop()

N = int(sys.stdin.readline().rstrip())
result = [0]
backTracking([])

try:
    print(sorted(result)[N-1])
except Exception:
    print(-1)
