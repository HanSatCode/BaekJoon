import sys

n = sys.stdin.readline().rstrip()

if len(n) == 2:
    print(int(n[0]) + int(n[1]))
elif len(n) == 3:
    if(n[-1] == "0") :
        print(int(n[0]) + int(n[1:]))
    else:
        print(int(n[:2]) + int(n[2]))
else : # 10 + 10
    print(20)