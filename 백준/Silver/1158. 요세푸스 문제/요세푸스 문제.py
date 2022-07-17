N, K = map(int, input().split())
Oli = [ x for x in range(1, N+1)]
li = [ x for x in range(1, N+1)]
r = []
cnt = -1

while len(r) != len(Oli) :
    for x in range(K) :
        cnt += 1
        if len(li)-1 < cnt :
            cnt = 0
            while 0 in li :
                li.remove(0)
    else :
        #print(li, li[cnt], cnt, r)
        while True :
            if len(li) == 1 :
                r.append(li[0])
                break
            elif li[cnt] == 0 :
                cnt += 1
            else :
                r.append(li[cnt])
                li[cnt] = 0
                break
else :
    print(f'<{str(r)[1:len(str(r))-1]}>')