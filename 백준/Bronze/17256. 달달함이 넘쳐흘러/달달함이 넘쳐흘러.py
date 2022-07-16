ax, ay, az = map(int, input().split())
bx, by, bz = map(int, input().split())

print(bx - az, int(by / ay), bz - ax)