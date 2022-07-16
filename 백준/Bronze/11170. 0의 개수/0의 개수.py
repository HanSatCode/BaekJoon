n = int(input())

for x in range(n) :
    r = 0
    a, b = map(int, input().split())
    for y in range(a, b+1) :
        if '0' in str(y) :
            r += list(str(y)).count('0')
    print(r)