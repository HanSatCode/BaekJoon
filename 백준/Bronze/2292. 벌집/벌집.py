n = int(input())
x = 1
block = 1

while (n > block) :
    block += 6 * x
    x += 1

print(x)