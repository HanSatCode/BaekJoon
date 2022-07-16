color = ['BWBWBWBW', 'WBWBWBWB']
chess = []
r = 32

N, M = map(int, input().split())

for _ in range(N) :
    chess.append(input())

for Ry in range(N-7) :
    for x in range(M-7) :
        r1 = r2 = 0
        for y in range(8) :
            temp = chess[y+Ry][x+0:x+8]
            if y % 2 != 0 :
                for a in range(8) :
                    if temp[a] != color[0][a] :
                        r1 += 1
                    elif temp[a] != color[1][a] :
                        r2 += 1
            else :
                for a in range(8) :
                    if temp[a] != color[1][a] :
                        r1 += 1
                    elif temp[a] != color[0][a] :
                        r2 += 1
        if r > r1 and r2 > r1 :
            r = r1
        elif r > r2 and r1 > r2 :
            r = r2
else :
    print(r)