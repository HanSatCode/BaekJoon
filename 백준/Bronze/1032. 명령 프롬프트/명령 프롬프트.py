from tabnanny import check


count = int(input())
words = []
checkAlphabet = []
result = ''

for x in range (0, count) :
    words.append(list(str(input())))

for x in range (0, len(words[0])) :
    for y in range(0, count) :
        checkAlphabet.append(words[y][x])

    checkAlphabet = set(checkAlphabet)
    checkAlphabet = list(checkAlphabet)

    if len(checkAlphabet) != 1 :
        result += '?'
    else :
        result += str(checkAlphabet[0])
    checkAlphabet = []

print(result)