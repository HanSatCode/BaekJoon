import sys

n = int(sys.stdin.readline().rstrip())
card = sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))), reverse=True)
result = 0

while len(card) != 1:
    result += card[0] + card.pop()
else:
    print(result)