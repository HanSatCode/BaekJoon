import sys

ISBN = sys.stdin.readline().rstrip()
checkSum = 0
checker = int(ISBN[-1])
weight = 0 # 가중치

for x in range(len(ISBN) - 1):
    if ISBN[x] == '*':
        weight = 3 if (x+1) % 2 == 0 else 1 # 홀수는 1, 짝수는 3
        continue
    checkSum += int(ISBN[x]) * (3 if (x+1) % 2 == 0 else 1)

for x in range(10):
    if (checkSum + (x * weight) + checker) % 10 == 0:
        print(x)
        break