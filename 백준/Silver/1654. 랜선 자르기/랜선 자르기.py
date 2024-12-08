import sys

K, N = map(int, sys.stdin.readline().rstrip().split(' '))
L = []
for _ in range(K):
    L.append(int(sys.stdin.readline().rstrip()))
else:
    MAX_LENGTH = sum(L) // N


first = 0
last = MAX_LENGTH

while last - first != 1:
    mid = (first + last) // 2
    L_sum = 0 
    for element in L :
        L_sum += element // mid
    if L_sum < N:
        last = mid
    else: #최대값을 찾기 때문에 중간 값을 딱 특정해서 찾을 필요가 없음 (아마)
        first = mid
else:
    if first == 0:
        print(1)
    else:
        check = []
        for num in [first, last]:
            temp = 0
            for element in L:
                temp += element // num
            else:
                check.append(temp)
        #print(first, last, check[0], check[1])
        if check[0] == check[1]:
            print(last)
        else:
            if check[1] < N:
                print(first)
            else:
                print(last)