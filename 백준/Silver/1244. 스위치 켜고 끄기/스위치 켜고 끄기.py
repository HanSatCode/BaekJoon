import sys

switch_N = int(sys.stdin.readline().strip('\n'))
switch = list(map(int, sys.stdin.readline().strip('\n').split()))
member = int(sys.stdin.readline().strip('\n'))

for _ in range(member) :
    s, n = map(int, sys.stdin.readline().strip('\n').split())
    
    if s == 1 : # 남자
        for x in range(n, len(switch)+1, n) :
            if switch[x-1] == 0 :
                switch[x-1] = 1
            else :
                switch[x-1] = 0
    else : # 여자
        if switch[n-1] == 0 :
            switch[n-1] = 1
        else :
            switch[n-1] = 0
        cnt = 0
        while True :
            if n-1-cnt == 0 or n-1+cnt == len(switch)-1 :
                break
            else :
                cnt += 1
                if switch[n-1+cnt] == switch[n-1-cnt] :
                    if switch[n-1+cnt] == 0 :
                        switch[n-1+cnt] = 1
                    else :
                        switch[n-1+cnt] = 0
                    if switch[n-1-cnt] == 0 :
                        switch[n-1-cnt] = 1
                    else :
                        switch[n-1-cnt] = 0
                else :
                    break
else :
    for x in range(1, switch_N+1) :
        if x % 20 == 0 :
            print(switch[x-1], end='\n')
        else :
            print(switch[x-1], end=' ')