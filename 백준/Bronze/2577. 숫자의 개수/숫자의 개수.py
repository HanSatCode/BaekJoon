A = int(input())
B = int(input())
C = int(input())
R = A*B*C
C = list(str(R))

z = 0

for x in range (0, 10) :
    for y in range (0, len(C)) :
        if int(C[y]) == x :
            z += 1
    print(z)
    z = 0