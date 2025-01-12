import sys

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

for alphabet in S:
    if alphabet == 'J':
        print('O', end='')
    elif alphabet == 'O':
        print('I', end='')
    else:
        print('J', end='')