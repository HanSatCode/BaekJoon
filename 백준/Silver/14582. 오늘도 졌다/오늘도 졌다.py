J = list(map(int, input().split()))
S = list(map(int, input().split()))
Js = 0
Ss = 0
counter = 0

for x in range(9) :
    Js += J[x]
    if Js > Ss :
        counter = 1
    Ss += S[x]
else :
    if Js < Ss and counter == 1 :
        print('Yes')
    else :
        print('No')