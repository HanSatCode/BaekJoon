count = int(input())

x = 0
a = 0
b = 0
memory = list()

for x in range(0, count) :
    a, b = input().split()
    memory.append([int(a),int(b)])

x = 0

for x in range(0, count) :
    print("Case #%d: %d" % (x+1, memory[x][0]+memory[x][1]))