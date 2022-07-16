n = int(input())
mem = []
x = 0
y = 0
z = 0
temp = 0
for x in range(0, n) :
    r = int(input())
    mem.append(r)

for x in range(0, n)  :
    for y in range(0, n)  :
        if mem[x] < mem[y] :
            temp = mem[x]
            mem[x] = mem[y]
            mem[y] = temp

for z in range(0, n)  :
    print(mem[z])