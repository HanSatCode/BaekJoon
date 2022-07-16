dict = {}
result = []
n = ''
w = '?'

while True :
    try : 
        w = input()
        n += w
    except EOFError:
        break

for word in n :
    dict[word] = dict.get(word, 0) + 1

if ' ' in dict :
    del dict[' ']

m = max(dict.values())
o = m

while o == m :
    r = max(dict, key=dict.get)
    result.append(r)
    del dict[r]
    if len(dict) == 0 :
        break
    else :
        o = max(dict.values())

result = sorted(result)

for x in result :
    print(x, end='')