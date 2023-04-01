import sys

scoreBoard = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
pointSum = 0.0
gradeSum = 0.0

for _ in range(20) :
    _, point, grade = sys.stdin.readline().split()
    if grade != "P" :
        if grade != "F" :
            gradeSum += float(point)*(4.5 - 0.5*scoreBoard.index(grade))
        pointSum += float(point)

print(format(gradeSum/pointSum, ".6f"))