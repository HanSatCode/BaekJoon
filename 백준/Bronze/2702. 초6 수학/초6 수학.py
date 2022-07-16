import math

num = []

t = int(input())

for x in range(0, t) :
    A, B = map(int, input().split())
    num.append([A, B])

for x in range(0, t) :
    print(math.lcm(num[x][0], num[x][1]), math.gcd(num[x][0], num[x][1]))
