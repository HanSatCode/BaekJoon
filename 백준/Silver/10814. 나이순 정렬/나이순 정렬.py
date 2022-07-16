num = int(input())
member = []

for x in range(num) :
    member.append(input().split())

member.sort(key = lambda x : int(x[0]))

for x in range(num) :
    print(member[x][0], member[x][1])