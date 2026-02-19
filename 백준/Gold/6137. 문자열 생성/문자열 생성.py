import sys

def answerPrint(string):
    for x in range(len(string)):
        print(string[x], end="")
        if (x + 1) % 80 == 0: print()

N =  int(sys.stdin.readline().strip())

S = ""
T = ""

left = 0
right = N - 1

for _ in range(N):
    S += sys.stdin.readline().strip()

while left <= right:
    if ord(S[left]) < ord(S[right]):
        T += S[left]; left += 1
    elif ord(S[left]) > ord(S[right]):
        T += S[right]; right -= 1
    else: # 만약에 양쪽이 같다면, 양쪽에서 한 글자씩 더 보면서 비교한다.
        temp_left = left + 1
        temp_right = right - 1
        while temp_left <= temp_right:
            if S[temp_left] == S[temp_right]: 
                temp_left += 1; temp_right -= 1
            elif ord(S[temp_left]) < ord(S[temp_right]):
                T += S[left]; left += 1; break
            else: # ord(S[temp_left]) > ord(S[temp_right])
                T += S[right]; right -= 1; break
        else: # 그래도 끝까지 같다면? 회문임.
            for i in range(left, (left + right) // 2 + 1): 
                T += (S[i] * 2)
            if (right - left + 1) % 2: T = T[:-1] # 홀수면 마지막 글자 하나 빼주기
            answerPrint(T)
            sys.exit(0)

answerPrint(T)