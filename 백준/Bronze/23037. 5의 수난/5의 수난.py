import math

n = int(input())
R = 0
for _ in range(5):
    R += math.pow(n % 10, 5)
    n = n // 10
print(int(R))