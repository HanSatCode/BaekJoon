n, k = list(map(int, input().split()))
a = b = 1

for x in range(n-k+1, n+1) :
    a *= x

for x in range(1, k+1) :
    b *= x

print(a//b)