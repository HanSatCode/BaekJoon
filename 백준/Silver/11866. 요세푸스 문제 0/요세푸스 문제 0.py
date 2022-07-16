n, k = map(int, input().split())
member = [ x for x in range(1, n+1) ]
result = []
index = -1

if k == 1 :
    result = [ x for x in range(1, n+1) ]
else :
    while len(member) != 1 :
        for _ in range(k) :
            if index == len(member)-1 :
                index = 0
                while '' in member :
                    member.remove('')
            else :
                index += 1
        else :
            result.append(member[index])
            member[index] = ''
    else :
        result.extend(member)
        while '' in result :
            result.remove('')

print('<', end='')
for x in range(n) :
    if x == n-1 :
        print(result[x], end='')
    else :
        print(result[x], end=', ')
print('>')