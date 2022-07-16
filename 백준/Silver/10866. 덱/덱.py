import sys
count = int(sys.stdin.readline())

d = []

for _ in range(count) :
    word = sys.stdin.readline().split()

    if word[0] == 'push_front' :
        d.insert(0, word[1])
    elif word[0] == 'push_back' :
        d.append(word[1])
    elif word[0] == 'pop_front' :
        if d :
            print(d[0])
            del d[0]
        else :
            print('-1')
    elif word[0] == 'pop_back' :
        if d :
            print(d[-1])
            del d[-1]
        else :
            print('-1')
    elif word[0] == 'size' :
        print(len(d))
    elif word[0] == 'empty' :
        if d :
            print('0')
        else :
            print('1')
    elif word[0] == 'front' :
        if d :
            print(d[0])
        else :
            print('-1')
    else :
        if d :
            print(d[-1])
        else :
            print('-1')