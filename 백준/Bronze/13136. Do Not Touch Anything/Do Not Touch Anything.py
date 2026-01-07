R, C, N = map(int, input().split(' '))
a = R // N if R % N == 0 else R // N + 1
b = C // N if C % N == 0 else C // N + 1
print(a * b)