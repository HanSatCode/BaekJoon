import sys

N, M = map(int, sys.stdin.readline().split(' '))
card = []
cnt = [0] * N
result = []


for n in range(N) :
    card.append(sorted(map(int, sys.stdin.readline().split(' ')), reverse=True))
else :
    for x in range(M):
        temp = []
        for y in range(N):
            temp.append(card[y][x])
        else :
            for y in range(N):
                if temp[y] == max(temp):
                    cnt[y] += 1
    else:
        #출력 로직 수정
        M = max(cnt)
        for x in range(N):
            if M == cnt[x]:
                result.append(str(x + 1))
        else:
            print(' '.join(result))
