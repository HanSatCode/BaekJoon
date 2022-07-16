n = int(input())
nL = list(map(int, input().split()))
m = int(input())
mL = list(map(int, input().split()))

nL.sort()

for x in mL :
    L_index = 0
    R_index = n-1

    while L_index <= R_index :
        M_index = (L_index + R_index) // 2

        if x == nL[M_index] :
            print('1')
            break

        elif x > nL[M_index] :
            L_index = M_index + 1

        else :
            R_index = M_index - 1
    
    else :
        print('0')