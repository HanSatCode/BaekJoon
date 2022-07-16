num = int(input())
word = []
temp = []
result = []
maxWordLen = 0
for x in range(num) :
    word.append(input())

word = set(word)
word = list(word)
maxWordLen = len(max(word, key=len))

for x in range(1, maxWordLen+1) :
    for y in range(len(word)) :
        if len(word[y]) == x :
            temp.append(word[y])
    temp.sort()
    result.extend(temp)
    temp.clear()

for x in range(len(result)) :
    print(result[x])
