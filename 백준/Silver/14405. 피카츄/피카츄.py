n = input()

while True :
    if n.find('pi') >= 0 :
        n = n.replace('pi', ' ')
    elif n.find('ka') >= 0 :
        n = n.replace('ka', ' ')
    elif n.find('chu') >= 0 :
        n = n.replace('chu', ' ')
    else :
        if len(n.strip()) == 0 :
            print('YES')
            break
        else :
            print('NO')
            break