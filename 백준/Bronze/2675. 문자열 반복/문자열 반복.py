t = int(input())

for x in range (t) :
    cir, ori = input().split()
    result = ""
    for x in ori :
        result += int(cir)*x
    print(result)