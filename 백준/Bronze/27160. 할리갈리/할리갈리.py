import sys

N = int(sys.stdin.readline().rstrip())
card = {}

for x in range(N):
    K, Y = map(str, sys.stdin.readline().rstrip().split(' '))
    card[K] = card.get(K, 0) + int(Y)
else:
    if 5 in card.values():
        print("YES")
    else:
        print("NO")