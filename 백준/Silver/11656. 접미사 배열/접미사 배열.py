import sys

S = sys.stdin.readline().strip('\n')
li = []

for x in range(0, len(S)) :
    li.append(S[x:])

li = sorted(li, key = lambda x : x)

for word in li :
    print(word)