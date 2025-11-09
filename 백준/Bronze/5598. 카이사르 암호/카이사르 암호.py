import sys

O = sys.stdin.readline().rstrip()

for element in O:
    ord_value = ord(element)
    if 65 <= ord_value <= 67:
        print(chr(23 + ord_value), end="")
    else:
        print(chr(ord_value - 3), end="")