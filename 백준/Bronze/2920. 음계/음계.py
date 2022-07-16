number = list(map(int, input().split()))
check = ""

if number[0] == 1 :
    for x in range (0, 8) :
        if number[x] != x+1 :
            check = "mixed"
            break
        else :
            check = "ascending"

elif number[0] == 8 :
    for x in range (0, 8) :
        if number[x] != 8-x :
            check = "mixed"
            break
        else :
            check = "descending"
            
else :
    check = "mixed"

print(check)