while True :
    a, b, c = input().split()
    MaxA = []

    MaxA.append(int(a))
    MaxA.append(int(b))
    MaxA.append(int(c))

    MaxR = max(MaxA)

    MaxA.remove(MaxR)
    
    if MaxR == 0 :
        break
    else :
        if MaxR**2 == MaxA[0]**2 + MaxA[1]**2 :
            print("right")
        else : 
            print("wrong")