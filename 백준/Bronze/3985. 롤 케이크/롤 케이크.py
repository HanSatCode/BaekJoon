import sys


L = int(sys.stdin.readline().rstrip())
bread = [ 0 for x in range(L) ]
M = 0
Ms = 0
R = 0
Rs = 0

N = int(sys.stdin.readline().rstrip())
for mem in range(N):
    P, K = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if Ms < (K - P) + 1:
        M = mem + 1
        Ms = (K - P) + 1
    temp = 0
    for index in range(P, K + 1):
        if not bread[index - 1]:
            temp += 1
        bread[index - 1] += 1
    if Rs < temp:
        R = mem + 1
        Rs = temp
    #print(bread, M, Ms, R, Rs)
else:
    print(M, R, sep="\n")