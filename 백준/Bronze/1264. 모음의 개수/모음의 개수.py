import sys

while True:
    cnt = 0
    temp = sys.stdin.readline().rstrip().lower()
    if temp == '#': break
    for element in temp:
        if element in ['a', 'e', 'i', 'o', 'u']: cnt += 1
    print(cnt)