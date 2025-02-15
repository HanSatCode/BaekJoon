import sys

def solve(presum, index):
    global price
    global selected_num

    if presum[0] >= target[0] and presum[1] >= target[1] and presum[2] >= target[2] and presum[3] >= target[3]:
        if price > presum[4]:
            price = presum[4]
            selected_num = [x + 1 for x in num]
    else:
        #print(f"선택된 것: {num} / 누적합 : {presum} / 최소 가격: {price}")
        for x in range(index, len(food)):
            if x in num:
                continue
            for y in range(5):
                presum[y] += food[x][y]
            num.append(x)
            solve(presum, x)
            for y in range(5):
                presum[y] -= food[x][y]
            num.pop()

N = int(sys.stdin.readline().rstrip())
target = []
food = []
presum = [0, 0, 0, 0, 0]
num = []

price = 7501
selected_num = []

for x in range(N + 1):
    if x == 0:
        target = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        continue
    food.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
else:
    solve(presum, 0)
    if price == 7501:
        print(-1)
    else:
        print(f"{price}\n{' '.join(map(str, selected_num))}")