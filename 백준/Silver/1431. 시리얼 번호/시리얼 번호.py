import sys

N = int(sys.stdin.readline().strip('\n'))
li = []

for _ in range(N) : 
    li.append(sys.stdin.readline().strip('\n'))

li = sorted(li, key=lambda x : (len(x), sum([int(y) for y in x if y.isnumeric()]), [ord(z) for z in x]))

for word in li :
    print(word)