n = input()

for word in n :
    ordASCII = int(ord(word))
    if (ordASCII >= 65 and ordASCII <= 90) or (ordASCII >= 97 and ordASCII <= 122) :
        if word.upper() == word :
            if ordASCII > 77 :
                tempOrdASCII = ordASCII - 78
                print(chr(tempOrdASCII + 65), end='')
            else :
                print(chr(ordASCII + 13), end='')
        else :
            if ordASCII > 109 :
                tempOrdASCII = ordASCII - 110
                print(chr(tempOrdASCII + 97), end='')
            else :
                print(chr(ordASCII + 13), end='')
    else :
        print(word, end='')