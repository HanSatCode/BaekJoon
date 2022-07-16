from itertools import count
import sys

counter = int(sys.stdin.readline())

for x in range (counter) :
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)