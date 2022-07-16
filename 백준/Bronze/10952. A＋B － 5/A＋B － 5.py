A = []
B = []
tempA = 1
tempB = 1
x = 0

while True :
    tempA, tempB = map(int,input().split())
    A.append(tempA)
    B.append(tempB)

    if tempA==0 and tempB==0 :
        break


while True :
    print(A[x]+B[x])
    x+=1

    if A[x]==0 and B[x]==0 :
        break