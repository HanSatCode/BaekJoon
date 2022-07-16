import sys

num = int(sys.stdin.readline().strip('\n'))
result = 0

for _ in range(num) :
    alpha = []
    word = sys.stdin.readline().strip('\n')
    for x in range(len(word)) :
        if word[x] not in alpha :
            alpha.append(word[x])
        else :
            if word[x-1] == word[x] :
                continue
            else :
                break
    else :
        result += 1
print(result)