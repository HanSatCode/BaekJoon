n = int(input())

for _ in range(n) :
    k = list(input().split())
    a, b = sorted(k[0]), sorted(k[1])
    if a == b :
        print(f'{k[0]} & {k[1]} are anagrams.')
    else :
        print(f'{k[0]} & {k[1]} are NOT anagrams.')