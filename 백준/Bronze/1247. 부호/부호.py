import sys
input = sys.stdin.readline

a = int(input())
aP = 0
for x in range(0, a) :
    aP += int(input())

b = int(input())
bP = 0
for x in range(0, b) :
    bP += int(input())

c = int(input())
cP = 0
for c in range(0, c) :
    cP += int(input())

if aP == 0 :
    print('0')
elif aP > 0 :
    print('+')
elif aP < 0 :
    print('-')

if bP == 0 :
    print('0')
elif bP > 0 :
    print('+')
elif bP < 0 :
    print('-')

if cP == 0 :
    print('0')
elif cP > 0 :
    print('+')
elif cP < 0 :
    print('-')