amount = int(input())
memberName = []
result = ''

for x in range (0, amount) :
    memberName.append(str(input())[:1])

for x in range(97, 123) :
    if memberName.count(chr(x)) >= 5:
        result += str(chr(x))

if result == '' :
    print('PREDAJA')
else :
    print(result)