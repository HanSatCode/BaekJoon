m, n = map(int, input().split())

for x in range(m, n+1) :
    if x == 1 :
        continue
    else :
        for y in range(2, int(x**(1/2)) + 1) : 
            if x%y == 0 :
                break
        else :
            print(x)