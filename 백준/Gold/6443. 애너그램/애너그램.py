# T/F로 사용/미사용 연산하면 시간초과뜸 -> dict 활용

import sys

def solve(checker, answer):
    global word

    if len(answer) == len(word):
        print(''.join(map(str, answer)))
        return
    else:
        for letter in checker.keys():
            # print(checker, letter)
            if checker[letter]: # 해당 알파벳을 사용할 수 있을 때
                checker[letter] -= 1
                solve(checker, answer + [letter])
                checker[letter] += 1
        return

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    word = sorted(sys.stdin.readline().rstrip())
    checker = dict()
    for letter in word:
        checker[letter] = checker.get(letter, 0) + 1
    solve(checker, [])