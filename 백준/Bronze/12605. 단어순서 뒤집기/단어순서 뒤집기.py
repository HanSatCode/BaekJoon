n = int(input())

for x in range(n) :
    m = list(input().split())
    m = m[::-1]
    print(f'Case #{x+1}: ', end='')
    for y in range(len(m)) :
        if y == len(m) - 1:
            print(m[y])
        else :
            print(m[y], end=' ')