N = int(input())

if N == 1 :
    print('1')
else :
    NL = [ x for x in range(2, N+1, 2) ]
    if N % 2 != 0 :
        NL.insert(0, N)
    while len(NL) > 2 :
        temp = NL[-1]
        # print(NL, temp)
        NL = [ NL[x] for x in range(1, len(NL), 2)]
        if NL[-1] != temp :
            NL.insert(0, temp)
    else :
        if len(NL) == 1 :
            print(NL[0])
        else :
            print(NL[1])