import sys

result = [x for x in range(0, 10)] # 한 자리는 그 수라고 바로 판단

def backTracking(list):
    if len(result) >= 500000:
        return
    else:
        for x in range(0, 10):
            list.append(x)
            if len(list) >= 2:
                if list[-1] < list[-2]: # 뒷자리의 계수가 앞자리의 계수보다 클 경우
                    result.append(int(''.join(map(str, list))))
                    backTracking(list)
            elif len(list) == 1:
                backTracking(list)
            list.pop()


N = int(sys.stdin.readline().rstrip())

if N >= 500000:
    print(-1)
else:
    backTracking([])
    try:
        result = sorted(result)
        # print(result)
        print(result[N])
    except Exception:
        print(-1)