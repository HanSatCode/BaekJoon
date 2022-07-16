from unittest import result


a = list(str(input()))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

res = []

for y in range (0, len(alphabet)) :
    for z in range (0, len(a)) :
        if alphabet[y] == a[z] :
            res.append(z)
            break
        if z == len(a)-1 :
            res.append('-1')

print(' '.join(map(str, res)))