import sys

N = int(sys.stdin.readline().strip())
P = list(map(int, sys.stdin.readline().strip().split()))
Player = {}
for x in P:
    if x == 0 : 
        continue
    Player[x] = Player.get(x, 0) + 1
else:
    Player = sorted(Player.items(), key=lambda x: x[1], reverse=True)
    print(Player[0][0] if Player[0][1] != Player[1][1] else "skipped")