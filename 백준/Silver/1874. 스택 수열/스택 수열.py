import sys

n = int(sys.stdin.readline().strip('\n'))
target = []
stack = []
cnt = 1

result = []
check = True

for _ in range(n) :
    target.append(int(sys.stdin.readline().strip('\n')))


while len(target) > 0 :
    if len(stack) > 0 :
        if cnt < n+1 :
            if target[0] != stack[-1] :
                stack.append(cnt)
                cnt += 1
                result.append('+')
            elif target[0] == stack[-1] :
                del target[0]
                del stack[-1]
                result.append('-')
        else : # cnt == n
            # if cnt not in stack and check :
            #     stack.append(cnt)
            #     result.append('+')
            #     check = False
            if target[0] == stack[-1] :
                del target[0]
                del stack[-1]
                result.append('-')
            else :
                print('NO')
                break

    else :
        stack.append(cnt)
        cnt += 1
        result.append('+')
        if target[0] == stack[-1] :
                del target[0]
                del stack[-1]
                result.append('-')

    #print(target, stack, cnt)
else :
    for symbol in result :
        print(symbol)