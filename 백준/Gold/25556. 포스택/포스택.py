import sys

N = int(sys.stdin.readline().strip())
T = list(map(int, sys.stdin.readline().strip().split()))
stack = [ [], [], [], [] ]

for element in T:
    for i in range(4):
        if stack[i] and stack[i][-1] < element:
            stack[i].append(element)
            break
        elif not stack[i]:
            stack[i].append(element)
            break
    else:
        print("NO")
        break
    #print(stack)
else:
    print("YES")