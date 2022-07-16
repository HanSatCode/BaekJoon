n = int(input())

for x in range(n) :
    l = []
    m = int(input())
    for y in range(m) :
        l.append(input().split())
    num = [ int(l[z][1]) for z in range(m) ]
    maxNum = num.index(max(num))
    print(l[maxNum][0])