N = input()
A = map(str, input().split())

cnt = 0
for element in A:
    if N in element:
        cnt += 1
print(cnt)