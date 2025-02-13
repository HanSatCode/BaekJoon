import sys
import time as t

cnt = 1
while True:
    problem = sys.stdin.readline().rstrip()
    if problem == '0':
        break
    else:
        if len(problem) % 2 != 0:
            print(f"Test {cnt}: {problem}")
            cnt += 1
            continue
        while True:
            result = ''
            for x in range(0, len(problem), 2):
                for y in range(int(problem[x])):
                    result += problem[x+1]
                #print(result)
            else:
                if len(result) % 2 != 0 or problem == result:
                    print(f"Test {cnt}: {result}")
                    cnt += 1
                    break
                problem = result