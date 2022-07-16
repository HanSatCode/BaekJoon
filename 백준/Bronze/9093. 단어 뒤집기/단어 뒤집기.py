n = int(input())
l = []

for x in range(n) :
    l.append(list(input().split()))

for x in range(n) :
    for y in range(len(l[x])) :
        if y == len(l[x]) -1 :
            print(l[x][y][::-1])
        else :
            print(l[x][y][::-1], end= ' ')