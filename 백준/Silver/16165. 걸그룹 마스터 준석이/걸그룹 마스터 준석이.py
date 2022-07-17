import sys

N, M = map(int, sys.stdin.readline().strip('\n').split())
group = []

for A_ in range(N) :
    team = sys.stdin.readline().strip('\n')
    member_N = int(sys.stdin.readline().strip('\n'))
    temp = []
    for B_ in range(member_N) :
        temp.append(sys.stdin.readline().strip('\n'))
    else :
        group.append([team, temp])

for C_ in range(M) :
    name = sys.stdin.readline().strip('\n')
    num = int(sys.stdin.readline().strip('\n'))
    for x in range(N) :
        if num == 0 : # 멤버 이름
            if name == group[x][0] :
                mem = sorted(group[x][1])
                for y in mem :
                    print(y, end='\n')
        else : # 팀 이름
            if name in group[x][1] :
                print(group[x][0])
                break