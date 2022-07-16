num = int(input())
inv = 666
counter = 0

while True :
    if str(inv).find('666') >= 0 :
        counter += 1

    if num == counter :
        break

    inv += 1

print(inv)