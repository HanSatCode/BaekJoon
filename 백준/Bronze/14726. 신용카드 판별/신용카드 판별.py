import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    x = sys.stdin.readline().strip()
    c = 0
    idx = 1
    for i in x[::-1]:
        i = int(i)
        if idx % 2 == 0:
            if i * 2 >= 10:
                c += ((i * 2) // 10) + ((i * 2) % 10)
            else:
                c += i * 2
        else:
            c += i
        idx += 1
    else:
        print("T" if c % 10 == 0 else "F")