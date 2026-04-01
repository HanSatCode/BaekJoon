import math
L = int(input())
A = int(input()); B = int(input())
C = int(input()); D = int(input())
print(L - math.ceil(max(A / C, B / D)))