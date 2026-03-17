A, B, C = map(int, input().split(' '))

result = sorted([A, B, C])

if len(set(result)) == 1: print(10000 + (result[0] * 1000))
elif len(set(result)) == 2: print(1000 + ((result[1] * 100)))
else: print(result[-1] * 100)