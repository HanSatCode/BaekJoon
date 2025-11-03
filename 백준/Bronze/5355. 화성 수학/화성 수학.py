import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    line = list(sys.stdin.readline().strip().split())
    base = float(line[0])
    for element in line[1:]:
        match element:
            case "@":
                base *= 3
            case "%":
                base += 5
            case "#":
                base -= 7
    print(f"{base:.2f}")