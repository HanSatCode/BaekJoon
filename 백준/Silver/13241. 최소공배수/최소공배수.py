import sys

a, b = map(int, sys.stdin.readline().split())

def g(x, y) :
    if x%y == 0 :
        return y
    return g(y, x%y)
             
r = g(a, b)
print(r * a//r * b//r)