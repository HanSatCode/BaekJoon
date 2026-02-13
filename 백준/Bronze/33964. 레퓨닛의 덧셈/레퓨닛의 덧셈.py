X, Y = map(int, input().split())
print("1" * abs(X - Y) + "2" * min(X, Y))