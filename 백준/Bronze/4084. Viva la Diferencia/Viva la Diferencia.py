while True:
    a, b, c, d = map(int, input().split())
    if a + b + c + d == 0: break
    cnt = 0
    while a != b or b != c or c != d:
        temp = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - temp)
        cnt += 1
    print(cnt)