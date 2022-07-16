n = int(input())
math = []
gap = -999

for x in range(n) :
    temp = list(map(int, input().split()))
    del temp[0]
    temp.sort()
    math.append(temp)

for x in range(1, n+1) :
    gap = -999
    for y in range(len(math[x-1])-1) :
        temp = math[x-1][y+1] - math[x-1][y]
        if temp > gap :
            gap = temp

    print(f'Class {x}')
    print(f'Max {max(math[x-1])}, Min {min(math[x-1])}, Largest gap {gap}')