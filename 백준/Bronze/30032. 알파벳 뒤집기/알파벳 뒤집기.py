import sys

element = {'d' : {1: 'q', 2: 'b'}, 'b' : {1: 'p', 2: 'd'}, 'q' : {1: 'd', 2: 'p'}, 'p' : {1: 'b', 2: 'q'}}

N, D = map(int, sys.stdin.readline().split())
for _ in range(N):
    temp = list(sys.stdin.readline().strip())
    for c in temp:
        print(element[c][D], end='')
    print()