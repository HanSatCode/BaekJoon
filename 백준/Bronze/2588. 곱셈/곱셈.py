a = int(input())
b = int(input())

print(a*(b%10))
print(str(a*(b%100-b%10))[:-1])
print(str(a*(b-b%100))[:-2])
print(a*b)