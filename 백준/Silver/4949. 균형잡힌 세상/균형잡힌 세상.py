import sys

while True :
    s = sys.stdin.readline().strip('\n')
    stack = []
    if s == '.' :
        break
    else :
        check = [ x for x in s if x in ['(', ')', '[', ']']]
        for x in check :
            if x == '(' or x == '[' :
                stack.append(x)
            elif x == ')' :
                if stack and stack[-1] == '(' :
                    stack.pop()
                else :
                    print('no')
                    break
            elif x == ']' :
                if stack and stack[-1] == '[' :
                    stack.pop()
                else :
                    print('no')
                    break
        else :
            if not stack :
                print('yes')
            else :
                print('no')