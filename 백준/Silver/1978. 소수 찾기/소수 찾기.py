x = 0
y = 0
number = []
numberNa = []
numberTempNa = 0
result = 0

count = int(input())

number = list(map(int, input().split()))

x = 0

for x in range(0, count) :
    for y in range(1, number[x]) :
        if number[x]%y == 0 :
            numberTempNa += 1
    numberNa.append(int(numberTempNa))
    numberTempNa = 0
    y = 0

x = 0

for x in range(0, count) :
    if numberNa[x] == 1 or numberNa == 2 :
        result += 1

print(result)