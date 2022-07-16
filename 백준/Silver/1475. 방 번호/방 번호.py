N = list(input())
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in N :
    x = int(x)
    if x == 6 or x == 9 :
        if result[6] <= result[9] :
            result[6] += 1
        else :
            result[9] += 1
    else :
        result[x] += 1
else : # 가장 많은 세트 수
    print(max(result))