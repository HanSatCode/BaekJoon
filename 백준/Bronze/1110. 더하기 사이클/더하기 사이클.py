n = input()
Cycle = 0
R = 0

while n != R :
    Cycle += 1
    if Cycle == 1 :
        if len(n) == 1 :
            n = str(0) + n
        tempA = int(n[0]) + int(n[1])
        if tempA < 10 :
            R = n[1] + str(tempA)
        else :
            R = n[1] + str(tempA)[1]
    else :
        if len(R) == 1 :
            n = str(0) + n
        tempA = int(R[0]) + int(R[1])
        if tempA < 10 :
            R = R[1] + str(tempA)
        else :
            R = R[1] + str(tempA)[1]
else :
    print(Cycle)