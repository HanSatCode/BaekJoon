A = list(map(int, input().split()))
B = list(map(int, input().split()))
R = 0

for x in range(10):
    if A[x] > B[x]: R += 1
    elif A[x] < B[x]: R -= 1
    else : pass
print("A" if R > 0 else "D" if R == 0 else "B")