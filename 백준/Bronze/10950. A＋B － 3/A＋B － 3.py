count = int(input())

x = 0
y = 0
a = 0
b = 0
memory = list()

for x in range(0, count) :
    a, b = input().split()
    memory.append([int(a),int(b)])

for y in range(0, count) :
    print(memory[y][0]+memory[y][1])