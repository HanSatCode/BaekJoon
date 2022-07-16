import math
T = int(input())
number = []

for x in range(0, T) :
    a, b = map(int, input().split())
    number.append([a,b])

for x in range(0, len(number)) :
    print(math.lcm(number[x][0], number[x][1]))