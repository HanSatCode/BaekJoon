n = int(input())
word = []
for x in range(n) :
    word.append(input())

for x in word :
    print(f'{x[0]}{x[-1]}')