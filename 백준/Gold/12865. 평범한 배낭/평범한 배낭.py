import sys

# N - 물건 수 / K - 품목 / E - 요소
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
E = [ [0, 0] ]
for _ in range(N):
    E.append(list(map(int, sys.stdin.readline().strip().split(' '))))

dp = [ [0] * (K + 1)  for _ in range(N + 1) ]
for order in range(1, N + 1):
    for left in range(1, K + 1):
        w = E[order][0] # 해당 순서의 물건 무게
        v = E[order][1] # 해당 순서의 물건 가치
        if left < w: # 만약, 담을 수 있는 최대 무게보다 물건의 무게 더 클 경우
            dp[order][left] = dp[order - 1][left] # 아무것도 못 담으니까 이전 순번의 최대 가치랑 똑같음
        else:
            # 안 담을 것인지, 이전 순번의 무게에서 현재 물건의 가치를 더한 것 중에서 최대 가치 선택
            dp[order][left] = max(dp[order - 1][left], v + dp[order - 1][left - w])
else:
    print(dp[N][K])