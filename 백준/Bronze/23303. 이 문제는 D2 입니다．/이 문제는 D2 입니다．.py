import sys

T = sys.stdin.readline().rstrip().lower()
try:
    a = T.index('d2')
    print('D2')
except:
    print('unrated')