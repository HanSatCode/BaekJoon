import sys

N = int(sys.stdin.readline().strip())
for x in range(N):
    L = list(sys.stdin.readline().strip().split())
    match(L[1]) :
        case "+":
            print("correct" if int(L[0]) + int(L[2]) == int(L[4]) else "wrong answer")
        case "-":
            print("correct" if int(L[0]) - int(L[2]) == int(L[4]) else "wrong answer")
        case "*":
            print("correct" if int(L[0]) * int(L[2]) == int(L[4]) else "wrong answer")
        case "/":
            print("correct" if int(L[0]) // int(L[2]) == int(L[4]) else "wrong answer")