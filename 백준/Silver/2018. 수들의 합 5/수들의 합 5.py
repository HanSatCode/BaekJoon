N = int(input()) # 메모리부족으로 누적합 제외

temp = 1
left = 1
right = 1
answer = 1

while right != N:
    if temp == N:
        answer += 1
        right += 1
        temp += right
    elif temp > N:
        temp -= left
        left += 1
    else:
        right += 1
        temp += right
print(answer)