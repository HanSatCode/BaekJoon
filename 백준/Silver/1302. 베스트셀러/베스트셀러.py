import sys

N = int(sys.stdin.readline().strip('\n'))
book = {}

for _ in range(N) :
    temp = sys.stdin.readline().strip('\n')
    book[temp] = book.get(temp, 0) + 1

print(sorted(book.items(), key = lambda x : (-x[1], x[0]))[0][0])