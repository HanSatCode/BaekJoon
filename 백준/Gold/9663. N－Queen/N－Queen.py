import sys

result = 0
N = int(sys.stdin.readline().rstrip())

def backtracking(L):
    global result

    if len(L) == N:
        result += 1
    else:
        for x in range(N):
            #print(L)
            L.append(x)
            # 상하끼리 같을 경우 or 대각선 관계 (가로 = 세로)
            for y in range(len(L) - 1):
                if x == L[y] or abs(x - L[y]) == abs(len(L) - 1 - y):
                    break
            else:
                backtracking(L)
            L.pop()

backtracking([])
print(result)