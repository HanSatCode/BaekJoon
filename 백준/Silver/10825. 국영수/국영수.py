import sys

N = int(sys.stdin.readline().strip('\n'))
score = [] # 이름 국 영 수

for _ in range(N) :
    n, k, e, m = sys.stdin.readline().strip('\n').split()
    score.append([n, int(k), int(e), int(m)])

score = sorted(score, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for name in score :
    print(name[0])