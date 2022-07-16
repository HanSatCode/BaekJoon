count = int(input())
li = []

for x in range(count) :
    num = input()
    if num == '0' :
        li.pop()
    else :
        li.append(int(num))

print(sum(li))