a, b, c = map(int, input().strip().split(' '))
a, b = abs(a), abs(b) # a, b 범위가 마이너스도 있다..
if a + b <= c:
    if c % 2 and (a + b) % 2 : print("YES") # 홀수
    elif (not c % 2) and (not ((a + b) % 2)) : print("YES") # 짝수 <- 출력실수...
    else : print("NO")
else : print("NO")