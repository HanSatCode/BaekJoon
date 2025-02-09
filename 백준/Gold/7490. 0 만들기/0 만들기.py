import sys

def dp(queue):
    #print(queue, eval(''.join(map(str,queue)).replace(" ", "") + '0'))
    if not queue:
        queue.append(1)
    else:
        queue.append(queue[-2] + 1)
    if len(queue) == (2 * case) - 1:
        if eval(''.join(map(str,queue)).replace(" ", "")) == 0:
            R.append(''.join(map(str,queue)))
    else:
        for math in ['+' , '-', ' ']:
            queue.append(math)
            dp(queue)
            queue.pop()
            queue.pop()
                

N = int(sys.stdin.readline().rstrip())
for x in range(N):
    case = int(sys.stdin.readline().rstrip())
    R = []
    dp([])
    R = sorted(R)
    for element in R:
        print(element)
    if x != N - 1:
        print()