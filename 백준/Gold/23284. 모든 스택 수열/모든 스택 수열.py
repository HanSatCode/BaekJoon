import sys
sys.setrecursionlimit(1000000)

def solve(i, n, stack, ans):
    if i > n and not stack:
        print(' '.join(map(str, ans)))
        return
    
    if stack:
        temp = stack.pop()
        ans.append(temp)
        solve(i, n, stack, ans)
        ans.pop()
        stack.append(temp)
    
    if i <= n:
        stack.append(i)
        solve(i + 1, n, stack, ans)
        stack.pop()
    

N = int(sys.stdin.readline().strip())
solve(1, N, [], [])