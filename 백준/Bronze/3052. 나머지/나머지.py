temp = 0
number = []
numberN = []
resultN = []
for x in range(0, 10) :
    temp = int(input())
    number.append(temp)

for x in range(0, 10) :
    numberN.append(number[x]%42)

resultSet = set(numberN)
resultN = list(resultSet)

print(len(resultN))