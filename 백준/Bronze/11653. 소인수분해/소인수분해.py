import sys
a = int(sys.stdin.readline())
x = 2
while True :
    if a%x == 0 :
        a /= x
        print(x)
        x = 2
    else :
        x += 1
    if a == 1 :
        break