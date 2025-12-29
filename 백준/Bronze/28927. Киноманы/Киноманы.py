a, b, c = map(int, input().split(' '))
d, e, f = map(int, input().split(' '))

M = (a * 3) + (b * 20) + (c * 120)
N = (d * 3) + (e * 20) + (f * 120)

print("Max" if M > N else "Mel" if M < N else "Draw")