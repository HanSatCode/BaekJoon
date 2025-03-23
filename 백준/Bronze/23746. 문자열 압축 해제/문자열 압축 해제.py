import sys

N = int(sys.stdin.readline().rstrip())
d = {}
for x in range(N):
    a, b = map(str, sys.stdin.readline().rstrip().split(' '))
    d[b] = a 
question = sys.stdin.readline().rstrip()
answer = ""
for element in question:
    answer += d[element]
else:
    S, E = map(int, sys.stdin.readline().rstrip().split(' '))
    print(answer[S-1:E])