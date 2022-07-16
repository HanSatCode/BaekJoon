import sys

n = int(input())
pw = []
pwR = []
for _ in range(n) :
    input_pw = sys.stdin.readline().strip('\n')
    pw.append(input_pw)
    pwR.append(input_pw[::-1])
    
r = [ x for x in pw if x in pwR ]
print(len(r[0]), (r[0])[len(r[0])//2])