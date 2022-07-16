a, b = input().split()
a, b = int(str(a)[::-1]), int(str(b)[::-1])
r = a + b
print(int(str(r)[::-1]))