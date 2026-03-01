N = input()
if int(N) <= 10: print(1)
else: 
    if int(N) >= int('1' * len(N)): print(len(N))
    else: print(len(N) - 1)