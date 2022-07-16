import collections

a = str(input()).upper()
check = []
for x in range (0, len(a)) :
    check.append(a[x])

if len(check) == 1 :
    print(check[0].upper())
    
else :
    if collections.Counter(check).most_common(2)[0][1] == collections.Counter(check).most_common(2)[1][1]:
        print("?")
    else : 
        print(collections.Counter(check).most_common(1)[0][0])