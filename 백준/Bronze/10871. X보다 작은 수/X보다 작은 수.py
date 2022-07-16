n, x = map(int, input().split())
li = list(map(int, input().split()))

for a in range(0, n):
    if li[a] < x:
        print(li[a], end = " ")