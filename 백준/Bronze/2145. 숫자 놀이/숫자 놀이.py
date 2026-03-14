import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0: break
    
    temp = n
    while temp // 10 != 0:
        cur = 0
        while temp != 0:
            cur += temp % 10
            temp = temp // 10
        temp = cur
    print(temp)