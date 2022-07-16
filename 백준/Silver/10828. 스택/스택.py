import sys
count = int(sys.stdin.readline())

stack = []

for x in range(count) :
    word = sys.stdin.readline().split()

    if word[0] == 'push' :
        stack.append(word[1])
    elif word[0] == 'pop' :
        if not stack :
            print('-1')
        else :
            print(stack[-1])
            stack.pop()
    elif word[0] == 'size' :
        print(len(stack))
    elif word[0] == 'empty' :
        if not stack :
            print('1')
        else :
            print('0')
    elif word[0] == 'top' :
        if not stack :
            print('-1')
        else :
            print(stack[-1])