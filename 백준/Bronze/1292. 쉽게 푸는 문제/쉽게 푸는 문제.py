A, B = map(int, input().split())
number = []
for x in range (1, 46) : # 대충 1035번째까지 나온다. 필요한건 1000번째까지
    number += [x] * x

print(sum(number[A-1 : B]))


'''원래 생각했던 쉬운 알고리즘. 100%에서 틀렸습니다 처리. 반례는 ?
A, B = map(int, input().split())
tempo = 1
result = 0

for x in range (1, B) :
    for y in range(0, x) :
        if tempo >= A and tempo<= B :
            result += x
        tempo += 1

print(result)'''