import sys

def recursion(start, n, x, y):
    if n == 1 :
        return start + (c % 2) + ((r % 2) * 2)
    
    horizonOver = 1 if c >= x - (2 ** (n - 1)) else 0 # 최대값에서 변 길이 빼기
    verticalOver = 2 if r >= y - (2 ** (n - 1))  else 0

    value = (horizonOver + verticalOver)

    x = x if horizonOver else x - (2 ** (n - 1))
    y = y if verticalOver else y - (2 ** (n - 1))
    
    start = start + (value * (4 ** (n - 1)))
    
    return recursion(start, n - 1, x, y)

N, r, c = map(int, sys.stdin.readline().split())

print(recursion(0, N, 2**N, 2**N))