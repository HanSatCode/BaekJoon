A, B, C = map(int, input().split())

for x in range(C) :
    A = (A % B) * 10
    R = A // B
else :
    print(R)