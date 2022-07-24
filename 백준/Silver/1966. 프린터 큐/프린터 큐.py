import sys

case = int(sys.stdin.readline().strip('\n'))

for _ in range(case) :
    doc, num = map(int, sys.stdin.readline().strip('\n').split())
    important = list(enumerate(list(map(int, sys.stdin.readline().strip('\n').split()))))
    cnt = 0
    current = tuple()
    target = important[num]
    while True :
        current = important[0]
        if important[0][1] < max([ x[1] for x in important ]) :
            important.append(important[0])
            del important[0]
        else :
            cnt += 1
            if important[0] == target :
                break
            else :
                del important[0]
    print(cnt)