n, Max = map(int, input().split())
li = list(map(int, input().split()))
R = []
for x in range(n) :
    for y in range(x+1, n) :
        for z in range(y+1, n) :
            S = li[x] + li[y] + li[z]
            if S > Max :
                continue
            else :
                R.append(S)
print(max(R))