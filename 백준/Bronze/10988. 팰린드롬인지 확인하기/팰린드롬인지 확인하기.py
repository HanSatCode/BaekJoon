import sys

s = list(str(input()))

for x in range(0, len(s)//2) :
    if s[x] != s[-(x+1)] :
        print('0')
        sys.exit(0)
print('1')