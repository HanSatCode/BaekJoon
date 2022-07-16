import sys

n = int(sys.stdin.readline().strip('\n'))

for _ in range(n) :
    l = []
    m = int(sys.stdin.readline().strip('\n'))
    for x in range(m) :
        l.append(int(sys.stdin.readline().strip('\n')))
    else :
        if len(set(l)) == 1 or l.count(max(l)) > 1 :
            print('no winner')
        else :
            lMax = l.index(max(l)) + 1
            l2 = sorted(l, reverse=True)
            if l2[0] > sum(l2[1:]) :
                print(f'majority winner {lMax}')
            elif l2[0] <= sum(l2)/2 :
                print(f'minority winner {lMax}')