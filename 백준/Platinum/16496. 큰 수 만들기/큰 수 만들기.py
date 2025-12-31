import sys

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))

# 다함께 10자리로 맞추면 쉬운 비교 가능 (우선 순위 가중치가 변하지 않음)
num = sorted(num, reverse=True, key = lambda x: (str(x) * 10)[:10])
result = ''.join(map(str, num))
if result[0] == '0':
    result = '0'
print(result)