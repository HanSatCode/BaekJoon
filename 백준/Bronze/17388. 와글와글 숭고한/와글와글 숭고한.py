T = list(map(int, input().strip().split(' ')))
if sum(T) >= 100: print("OK")
else:
    m = T.index(min(T))
    print("Soongsil" if m == 0 else "Korea" if m == 1 else "Hanyang")