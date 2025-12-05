import sys

d = {"animal" : "Panthera tigris", "tree" : "Pinus densiflora", "flower" : "Forsythia koreana"}

while True:
    line = sys.stdin.readline().strip()
    if line == "end":
        break
    print(d[line])