import sys

N = int(input())

while True:
    temp = int(input())
    if temp == 0: break
    if (temp % N == 0): print(f"{temp} is a multiple of {N}.")
    else: print(f"{temp} is NOT a multiple of {N}.")