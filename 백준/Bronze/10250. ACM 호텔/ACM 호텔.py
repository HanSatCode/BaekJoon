repeat = int(input())
number = []

for x in range (repeat) :
    H, W, N = map(int, input().split())
    number.append([H, W, N])

for x in range (0, repeat) :
    if number[x][2]%number[x][0] == 0 :
        topResult = number[x][0]
        bottomResult = number[x][2]//number[x][0]
    else :
        topResult = number[x][2]%number[x][0]
        bottomResult = number[x][2]//number[x][0]+1
    print(str(topResult) + str(bottomResult).zfill(2))