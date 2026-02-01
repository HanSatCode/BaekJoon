import sys

N = int(sys.stdin.readline().strip())
for x in range(N):
    D = {}
    text = sys.stdin.readline().strip()
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            D[char_lower] = D.get(char_lower, 0) + 1
    if len(D) == 0: 
        print(f"Case {x+1}: Not a pangram")
        continue
    max_count = max(D.values())
    min_count = min(D.values())
    if len(D) != 26 or min_count == 0: print(f"Case {x+1}: Not a pangram")
    elif len(D) == 26 and min_count == 1: print(f"Case {x+1}: Pangram!")
    elif len(D) == 26 and min_count == 2: print(f"Case {x+1}: Double pangram!!")
    else: print(f"Case {x+1}: Triple pangram!!!")