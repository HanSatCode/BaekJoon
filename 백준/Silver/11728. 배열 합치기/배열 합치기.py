A, B = map(int, input().split())
num = []
numR = []
for x in range(2) :
    num.append(list(map(int, input().split())))

for x in range(0, A) :
    numR.append(num[0][x])

for x in range(0, B) :
    numR.append(num[1][x])

numR = sorted(numR)

for x in range(0, len(numR)) :
    print(numR[x], end = ' ')