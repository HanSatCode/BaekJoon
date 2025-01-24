import sys

K = sys.stdin.readline().rstrip()

if len(K) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    init = int(K[0]) - int(K[1])
    for x in range(1, len(K)-1):
        comp = int(K[x]) - int(K[x + 1])
        if init != comp:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
    else:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")