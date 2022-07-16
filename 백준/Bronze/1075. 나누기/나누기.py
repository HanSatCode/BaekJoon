n = int(input())
f = int(input())

n -= int(str(n)[-2:])

while True :
    if n%f == 0 :
        print(str(n)[-2:])
        break
    else :
        n += 1