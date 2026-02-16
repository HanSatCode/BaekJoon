import sys

def judge(left, right, T):
    while left < right:
        if T[left] != T[right]: return False
        else: left += 1; right -= 1
    return True

N = int(sys.stdin.readline().strip())
for _ in range(N):
    T = list(sys.stdin.readline().strip())
    leftPointer = 0; rightPointer = len(T) - 1

    while leftPointer < rightPointer:
        if T[leftPointer] != T[rightPointer]:
            # 앞에서 검사한건 이미 회문이라고 판단했으므로, 안에만 검사함.
            if judge(leftPointer + 1, rightPointer, T) or judge(leftPointer, rightPointer - 1, T): print("1"); break
            else: print("2"); break
        else: leftPointer += 1; rightPointer -= 1
    else: print("0") # 회문