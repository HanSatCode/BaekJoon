import sys
M = int(sys.stdin.readline().strip('\n'))

S = set()

for _ in range(M) :
    try :
        DEF_List = list(sys.stdin.readline().strip('\n').split())
        DEF = DEF_List[0]
        num = int(DEF_List[1])
        if DEF == 'add' :
            if num in S :
                continue
            else :
                S.add(num)
        elif DEF == 'remove' :
            if num not in S :
                continue
            else :
                S.remove(num)
        elif DEF == 'check' :
            if num in S :
                print('1')
            else :
                print('0')
        elif DEF == 'toggle' :
            if num in S :
                S.remove(num)
            else :
                S.add(num)
    except :
        if DEF == 'all' :
            S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        else :
            S.clear()