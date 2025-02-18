import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    _ = sys.stdin.readline()
    Sc, Bc = map(int, sys.stdin.readline().rstrip().split(' '))
    S = sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))), reverse=True)
    B = sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))), reverse=True)
    
    while True:
        try:
            if S[-1] >= B[-1]:
                B.pop()
            else:
                S.pop()
        except Exception:
            break
    print('S' if not len(S) == 0 else 'B')