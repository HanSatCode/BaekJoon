import sys

queue = []

n = int(sys.stdin.readline().strip())

for _ in range(n) :
    temp = list(map(int, sys.stdin.readline().strip().split()))
    if temp == [0] :
        if queue == [] :
            print('-1')
        else :
            print(max(queue))
            queue.remove(max(queue))
    else :
        queue.extend(temp[1:])