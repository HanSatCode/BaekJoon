import sys

answer = [13, 14, 34]
q = set()

N = int(sys.stdin.readline().strip())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    q.add(10 * a + b if a < b else 10 * b + a)
else:
    if answer == sorted(list(q)):
        print("Wa-pa-pa-pa-pa-pa-pow!")
    else:
        print("Woof-meow-tweet-squeek")