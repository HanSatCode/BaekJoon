import sys

n = int(sys.stdin.readline().strip('\n'))
li = []

for _ in range(n) :
    name, day, month, year = sys.stdin.readline().strip('\n').split()
    li.append([name, int(day), int(month), int(year)])

li = sorted(li, key=lambda x : (x[3], x[2], x[1]))

print(li[-1][0])
print(li[0][0])