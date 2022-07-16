subjectCount = int(input()) # 필요는 없지만 문제풀때 필요한거
subject = list(map(int, input().split()))
nAt = 0
max = 0

x = 0

for x in range(0, subjectCount) :
    if max < subject[x] :
        max = subject[x]

x = 0

for x in range(0, subjectCount) :
    subject[x] = subject[x]/max*100
    nAt += subject[x]

print(nAt/len(subject))