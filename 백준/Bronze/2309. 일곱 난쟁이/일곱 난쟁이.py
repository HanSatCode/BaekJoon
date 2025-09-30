import sys

def solve(List, per):
    global L
    if per == 100 and len(List) == 2:
        for x in sorted([ x for x in L if x not in List]):
            print(x)
        sys.exit(0)
    elif per > 100:
        return
    else:
        for x in range(len(List)):
            temp = List.pop(x)
            solve(List, per + temp)
            List.insert(x, temp)

L = []
for x in range(9):
    L.append(int(sys.stdin.readline().rstrip()))

solve(sorted(L), 0)