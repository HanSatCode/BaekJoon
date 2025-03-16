n = 0
while True:
    try:
        t = input()
        n += 1
    except EOFError:
        print(n)
        break