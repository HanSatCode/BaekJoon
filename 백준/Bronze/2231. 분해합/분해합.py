num = int(input())
result = 0

for x in range(1, num+1) :
    sumsum = x + sum(list(map(int, str(x))))
    if sumsum == num :
        result = x
        break
print(result)