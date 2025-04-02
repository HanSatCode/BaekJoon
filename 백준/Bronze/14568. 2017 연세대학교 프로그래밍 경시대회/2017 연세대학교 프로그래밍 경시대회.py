import sys

result = 0

n  = int(sys.stdin.readline().rstrip())

for x in range(1, n): #택희
    for y in range(1, n-x): #영훈
        for z in range(1, n-y): #남규
            if (x+y+z == n) and (x%2 == 0) and (x*y*z != 0) and (z >= y + 2):
                #print(x, y, z)
                result += 1
else:
    print(result)