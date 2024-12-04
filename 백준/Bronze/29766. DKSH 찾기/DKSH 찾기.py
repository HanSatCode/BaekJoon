import sys

S = sys.stdin.readline().rstrip()
index = 0
result = 0

while index <= len(S):
    if S[index:index + 4] == "DKSH":
        result += 1
        index += 4
    else:
        index += 1
else:
    print(result)