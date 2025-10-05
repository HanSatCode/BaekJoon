import sys

N = list(map(int, sys.stdin.readline().strip().split()))
i = 1

while True:
    cnt = [ True for x in N if i % x == 0]
    if len(cnt) >= 3:      
        print(i)
        break
    i += 1