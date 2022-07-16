n = []

while True :
    addNumber = str(input())
    if addNumber[0] == "0" :
        break
    else :
        n.append(addNumber)

for x in range(0, len(n)) :
    z = 1
    if len(n[x])%2 == 0 :
        for y in range(0, len(n[x])) :
            if n[x][y] != n[x][-z] :
                print("no")
                break
            elif len(n[x])/2 <= y+1 :
                print("yes")
                break
            z += 1

    else :
        for y in range(0, len(n[x])) :
            if n[x][y] != n[x][-z] :
                print("no")
                break
            elif len(n[x])/2 <= y+1 :
                print("yes")
                break
            z += 1