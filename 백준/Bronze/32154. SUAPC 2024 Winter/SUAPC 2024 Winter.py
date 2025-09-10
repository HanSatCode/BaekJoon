import sys

DB = [['I', 'K'], ['B', 'D', 'J', 'K'], ['B', 'D', 'J', 'K'],
      ['D','I','J','K'], ['B','D','I','J','K'], ['B','D','I','J','K'],
      ['B','D','I','J','K'], ['B','D','I','J','K'], ['B','D','I','J','K'],
      ['D','E','I','J','K']
]
N = int(sys.stdin.readline().strip())

print(13 - len(DB[N-1]))
for c in "ABCDEFGHIJKLM":
    if c not in DB[N-1]:
        print(c, end=' ')