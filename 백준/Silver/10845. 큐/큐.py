import queue
import sys
count = int(sys.stdin.readline())

q = []

for _ in range(count) :
    word = sys.stdin.readline().split()

    if word[0] == 'push' :
        q.append(word[1])

    elif word[0] == 'pop' :
        if q :
            print(q[0])
            del q[0]
        else :
            print('-1')

    elif word[0] == 'size' :
        print(len(q))

    elif word[0] == 'empty' :
        if not q :
            print('1')
        else :
            print('0')

    elif word[0] == 'front' :
        if q :
            print(q[0])
        else :
            print('-1')
    
    else :
        if q :
            print(q[-1])
        else :
            print('-1')