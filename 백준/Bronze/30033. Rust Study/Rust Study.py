N = int(input())
A = list(map(int, input().strip().split(' ')))
B = list(map(int, input().strip().split(' ')))
r = 0
for x in range(N):
    if A[x] <= B[x]: r += 1
print(r)