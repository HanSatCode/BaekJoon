import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    X = int(A, 2) ^ int(B, 2)
    print("Hamming distance is " + str(bin(X).count("1")) + ".")
