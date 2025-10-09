import sys

S = {'K' : 0, 'Q' : 9, 'R' : 5, 'B' : 3, 'N' : 3, 'P' : 1,}
R = 0

for x in range(8):
    temp = sys.stdin.readline().strip()
    for y in range(8) :
        if temp[y] ==  temp[y].upper(): # 대문자일경우
            R += S.get(temp[y], 0)
        else: # 소문자일경우
            R -= S.get(temp[y].upper(), 0)
else:
    print(R)