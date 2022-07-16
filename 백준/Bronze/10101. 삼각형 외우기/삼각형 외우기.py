angle = []
for x in range (0, 3) :
    angle.append(int(input()))

if angle[0] + angle[1] + angle[2] == 180 :
    if angle[0] == angle[1] == angle[2] :
        print('Equilateral')
    else :
        if angle[0] == angle[1] or angle[0] == angle[2] or angle[1] == angle[2] :
            print('Isosceles')
        else :
            print('Scalene')
else :
    print('Error')