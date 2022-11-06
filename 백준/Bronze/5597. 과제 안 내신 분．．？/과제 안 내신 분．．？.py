import sys
sub = [int(sys.stdin.readline()) for _ in range(28)]
for x in range(1, 31) :
    if not x in sub :
        print(x)