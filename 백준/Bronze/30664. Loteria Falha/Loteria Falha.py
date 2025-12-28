while(True) :
    temp = int(input())
    if temp == 0:
        break
    if temp % 42 == 0:
        print("PREMIADO")
    else :
        print("TENTE NOVAMENTE")