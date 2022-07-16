n = int(input())
num = []
avg = []

for x in range(n) :
    num.append(list(map(int, input().split())))
    avg.append(sum(num[x][1:]) / num[x][0])
    tempA = [ y for y in num[x][1:] if avg[x] < y ]
    result = round((len(tempA)/num[x][0])*100, 3)
    print(f'{result:.3f}%')