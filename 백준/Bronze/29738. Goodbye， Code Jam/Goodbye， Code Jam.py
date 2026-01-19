import sys

N = int(sys.stdin.readline().strip())
for x in range(N):
    R = int(sys.stdin.readline().strip())
    print(f"Case #{x + 1}: ", end = "")
    if R <= 25: print("World Finals")
    elif R <= 1000: print("Round 3")
    elif R <= 4500: print("Round 2")
    else: print("Round 1")