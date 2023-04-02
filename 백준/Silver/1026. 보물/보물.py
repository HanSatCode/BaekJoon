import sys

result = 0

n = sys.stdin.readline().strip('\n')

a = list(map(int, sys.stdin.readline().strip('\n').split()))
b = list(map(int, sys.stdin.readline().strip('\n').split()))

a.sort(reverse = True)
b.sort()

for x in range(len(a)) :
    result += a[x] * b[x]
    
print(result)