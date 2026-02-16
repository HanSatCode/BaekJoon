import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    T = list(sys.stdin.readline().strip())
    leftPointer = 0; rightPointer = len(T) - 1

    while leftPointer < rightPointer:
        if T[leftPointer] != T[rightPointer]:
            LM = T[:leftPointer] + T[leftPointer + 1:] # 왼쪽을 바꿔보자
            RM = T[:rightPointer] + T[rightPointer + 1:] # 오른쪽을 바꿔보자
            if LM == LM[::-1] or RM == RM[::-1]: print("1"); break
            else: print("2"); break
        else: leftPointer += 1; rightPointer -= 1
    else: print("0") # 회문