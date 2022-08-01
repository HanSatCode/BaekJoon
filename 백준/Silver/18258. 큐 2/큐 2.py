import sys
from collections import deque

N = int(sys.stdin.readline().strip('\n'))
Q = deque() # 훨씬빠른 덱

def push(n) :
    Q.append(int(n))

def pop() :
    if not Q : print(-1)
    else :
        print(Q[0])
        Q.popleft()

def size() : 
    print(len(Q))

def empty() :
    if not Q : print(1)
    else : print(0)

def front() :
    if not Q : print(-1)
    else : print(Q[0])

def back() : # back
    if not Q : print(-1)
    else : print(Q[-1])

for _ in range(N) :
    j = sys.stdin.readline().strip('\n').split()

    if j[0] == 'push' :
        push(j[1])
    elif j[0] == 'pop' :
        pop()
    elif j[0] == 'size' :
        size()
    elif j[0] == 'empty' :
        empty()
    elif j[0] == 'front' :
        front()
    else : # back
        back()