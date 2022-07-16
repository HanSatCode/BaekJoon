a, b = map(str, input().split())
A = list(a)
B = list(b)
temp = A[0]
A[0] = A[2]
A[2] = temp
temp = B[0]
B[0] = B[2]
B[2] = temp
reA = ''.join(A)
reB = ''.join(B)
if reA > reB :
    print(reA)
elif reA < reB :
    print(reB)