N = int(input())
P = sorted(map(int, input().split()))
tempSum = sum = 0
for x in range(N) :
    tempSum += P[x]
    sum += tempSum
print(sum)