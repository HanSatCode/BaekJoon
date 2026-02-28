import sys

cnt = 1

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0: break
    n4 = (((3 * n + 1) // 2) * 3) // 9
    if (n % 2 == 0): print(f"{cnt}. even {n4}")
    else: print(f"{cnt}. odd {n4}")
    cnt += 1