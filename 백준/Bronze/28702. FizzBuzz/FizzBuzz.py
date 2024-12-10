import sys

target = 0

for x in range(3):
    temp = sys.stdin.readline().rstrip();
    if temp.isdigit():
        target = int(temp) + (3 - x)
else:
    if target % 3 == 0:
        if target % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if target % 5 == 0:
            print("Buzz")
        else:
            print(target)