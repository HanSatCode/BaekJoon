import sys

a, b = map(int, sys.stdin.readline().rstrip().split(' '))

result = 1
sum = sum([ x for x in range(1, a)])

for x in range(a, b + 1) : 
    sum += x
    result = result * sum
else:
    print(result % 14579)