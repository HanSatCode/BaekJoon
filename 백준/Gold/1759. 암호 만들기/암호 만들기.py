import sys

def backTracking(list):
    if len(list) == L:
        vowel = 0 # 모음 카운트 (최소 1개 이상)
        consonant = 0 # 자음 카운트 (최소 2개 이상)
        for m in list: # 로직을 거꾸로 구현해놔서 틀렸습니다 뜸..
            if m in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
            else:
                consonant += 1
        else:
            #print(list, vowel, consonant)
            if vowel >= 1 and consonant >= 2:
                print(''.join(map(str, list)))
    else:
        for letter in pwd:
            list.append(letter)
            if len(list) >= 2: # 리스트 길이가 2 이상
                if list[-1] > list[-2]: # 앞에거보다 뒤에것이 클 경우
                    backTracking(list)
            elif len(list) == 1:
                backTracking(list)
            list.pop()


L, C = map(int, sys.stdin.readline().rstrip().split(' '))
pwd = sorted(list(map(str, sys.stdin.readline().rstrip().split(' '))))
backTracking([])