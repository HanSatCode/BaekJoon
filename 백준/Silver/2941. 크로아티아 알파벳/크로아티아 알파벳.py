import sys

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().strip('\n')

for x in cro :
    word = word.replace(x, '!')

print(len(word))