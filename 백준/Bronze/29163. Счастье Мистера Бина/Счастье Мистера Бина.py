import sys

n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

for element in num:
    if element % 2 == 0:
        cnt += 1
else:
    if(cnt / n) > 0.5:
        print("Happy")
    else:
        print("Sad")