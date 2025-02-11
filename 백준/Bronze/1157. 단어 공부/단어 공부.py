import sys

S = sys.stdin.readline().rstrip()
D = dict()

for word in S:
    D[word.upper()] = D.get(word.upper(), 0) + 1
else:
    if len(D) == 1:
        print(list(D.items())[0][0])
    else:
        D = sorted(D.items(), key=lambda x: x[1], reverse=True)[:2]
        if list(D[0])[1] == list(D[1])[1]:
            print('?')
        else:
            print(list(D[0])[0])