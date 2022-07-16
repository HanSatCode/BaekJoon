sen = input()
count = 0
count_E = 0
while count_E < len(sen) :
    print(sen[count], end='')
    count += 1
    count_E += 1
    if count % 10 == 0 :
        print()