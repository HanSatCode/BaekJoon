import sys

N = int(sys.stdin.readline().strip())
parent = [-1 for i in range(N + 1)]
queue = [1] # 루트노드
L = dict()

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    L[a] = L.get(a, []) + [b]
    L[b] = L.get(b, []) + [a]
else:
    while queue:
        current = queue.pop(0)
        for child in L[current]:
            if parent[child] == -1:
                parent[child] = current
                queue.append(child)
                
    for element in range(2, N + 1):
        print(parent[element])