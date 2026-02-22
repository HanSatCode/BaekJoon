import sys

while True:
    A = int(sys.stdin.readline().strip())
    if A == 0: break
    cnt = 0
    for x in range(1, A):
        if (A ** 2) % x == 0:
            B = (A ** 2 // x) - x
            if B % 2 == 0: 
                if B // 2 > A: cnt += 1
                else: break
    print(cnt)