m = int(input())
n = int(input())
sosu = []
resultSum = 0

for x in range(m, n+1) :
    check = 0
    for y in range(2, x) :
        if x%y == 0 :
            check += 1
            break
    if check == 0 :
        sosu.append(x)

if 1 in sosu :
    sosu.remove(1)

if len(sosu) == 0 :
    print("-1")

else :
    print(sum(sosu))
    print(min(sosu))