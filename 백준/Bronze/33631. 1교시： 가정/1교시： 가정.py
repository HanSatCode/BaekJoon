import sys

flur, chocolate, egg, butter = map(int, sys.stdin.readline().split())
nFlur, nChocolate, nEgg, nButter = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

p = 0

for _ in range(N):
    select, element = map(int, sys.stdin.readline().split())
    if select == 1: # make cake element
        if flur >= (nFlur * element) and chocolate >= (nChocolate * element) and egg >= (nEgg * element) and butter >= (nButter * element):
            p += element
            flur -= (nFlur * element)
            chocolate -= (nChocolate * element)
            egg -= (nEgg * element)
            butter -= (nButter * element)
            print(p)
        else:
            print("Hello, siumii")
    elif select == 2: # add flur
        flur += element
        print(flur)
    elif select == 3: # add chocolate
        chocolate += element
        print(chocolate)
    elif select == 4: # add egg
        egg += element
        print(egg)
    elif select == 5: # add butter
        butter += element
        print(butter)