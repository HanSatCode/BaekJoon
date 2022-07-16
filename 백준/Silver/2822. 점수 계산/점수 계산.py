n = []

for x in range(8) :
    n.append(int(input()))

nSort = sorted(n, reverse=True)[:5]
sum = sum(nSort)

R = [ n.index(y)+1 for y in n if y in nSort ]

print(sum)

for z in R :
    print(z, end=' ')