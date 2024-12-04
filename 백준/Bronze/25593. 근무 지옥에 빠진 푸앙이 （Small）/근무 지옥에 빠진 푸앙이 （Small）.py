import sys

N = int(sys.stdin.readline().rstrip())
member = {}
time = [4, 6, 4, 10]

for x in range(N):
    for t in time:
        temp = list(map(str, sys.stdin.readline().rstrip().split(' ')))
        for target in temp:
            if target == '-':
                continue
            member[target] = member.get(target, 0) + t
else:
    #한명만 말뚝세우면 불공평한 것인가..?
    if len(member) < 1:
        print("Yes")
    else:
        m = member.values()
        if min(m) + 12 < max(m):
            print("No")
        else:
            print("Yes")