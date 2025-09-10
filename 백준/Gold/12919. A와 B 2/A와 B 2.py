import sys

def solve(cur):
    if cur == S:
        print(1)
        sys.exit()
    else:
        if len(cur) == len(S):
            return
        if cur[-1] == "A":
            solve(cur[:-1])
        if cur[0] == "B":
            solve(cur[1:][::-1])
    
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

solve(T)
print(0) # 못찾으면 0 출력