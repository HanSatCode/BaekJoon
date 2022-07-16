number = [['A', 'B', 'C'], ['D','E','F'], ['G','H','I'], ['J', 'K', 'L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]
result = 0

alphabet = list(str(input()))

for x in range(0, len(alphabet)) :
    for y in range(0, 8) :
        if alphabet[x] in number[y]  :
            result += y + 2
            break

print(result+len(alphabet))