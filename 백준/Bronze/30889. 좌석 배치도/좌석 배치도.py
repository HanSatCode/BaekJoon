N = int(input())
T = []

for _ in range(N):
    temp = input()  
    T.append((ord(temp[0]) - 65) * 20 + int(temp[1:]))

for x in range(10):
    for y in range(1, 21):
        if x * 20 + y in T: print("o", end = "")
        else: print(".", end = "")
    print("")