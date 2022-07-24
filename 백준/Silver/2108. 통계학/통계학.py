import sys

N = int(sys.stdin.readline().strip('\n'))
bin = {}
li = []

for _ in range(N) :
    temp = int(sys.stdin.readline().strip('\n'))
    bin[temp] = bin.get(temp, 0) + 1
    li.append(temp)

print(f'{round(sum([key*value for key, value in bin.items()])/N)}') # 산술평균

print(f'{sorted(li)[N//2]}') # 중앙값

a = [ key for key, value in bin.items() if value == max(bin.items(), key=lambda x : x[1])[1] ] # 최빈값

if len(a) > 1 :
    print(sorted(a)[1])
else :
    print(a[0])

print(f'{max(li)-min(li)}')