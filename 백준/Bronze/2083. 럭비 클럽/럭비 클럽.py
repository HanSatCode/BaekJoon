import sys

while(True):
    temp = list(map(str, sys.stdin.readline().strip().split(' ')))
    if temp == ['#', '0', '0']: break
    if int(temp[1]) > 17 or int(temp[2]) >= 80: print(temp[0], "Senior")
    else: print(temp[0], "Junior")