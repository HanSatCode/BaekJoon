x = 0
z = 0
number = []
for x in range (0, 9) :
    z = int(input())
    number.append(int(z))
print(max(number))
print(int(number.index(max(number)))+1)