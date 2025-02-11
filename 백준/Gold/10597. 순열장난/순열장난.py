import sys
import time as t

def dp(list) :
    global index
    if len(''.join(map(str, list))) == len(S):
        temp = sorted(list)
        if temp == [ x for x in range(1, temp[-1] + 1)]:
            print(*list, end = ' ')
            exit()
    for length in range(len(S[index:])):
        element = int(S[index:index + length + 1])
        #print(list, element)
        if element in list:
            continue
        elif element > 50:
            break
        list.append(element)
        index += length + 1
        dp(list)
        index -= length + 1
        list.pop()

S = sys.stdin.readline().rstrip()
index = 0
dp([])