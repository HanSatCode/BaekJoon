import sys

origin = sys.stdin.readline().rstrip()
stack = []


for word in origin:
    stack.append(word)
    if len(stack) >= 4:
        # print(''.join(stack[-4:]))
        if ''.join(stack[-4:]) == 'PPAP':
            for _ in range(3):
                stack.pop()
else:
    if ''.join(stack) == 'P':
        print('PPAP')
    else:
        print('NP')