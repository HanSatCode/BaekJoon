while True:
    try :
        N, M = map(int, input().split(' '))
        print(M // (N + 1))
    except :
        break
    