import sys

K = int(sys.stdin.readline().rstrip())

for x in range(K):
    print("G" * K + "." * K * 3)
for x in range(K):
    print("." * K + "I" * K + "." * K + "T" * K)
for x in range(K):
    print("." * 2 * K + "S" * K + "." * K)