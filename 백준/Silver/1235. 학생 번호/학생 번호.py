student = []
moduler = 10

cnt = int(input())
for _ in range(cnt) :
    student.append(input())

for length in range(1, len(student[0])+1) :
    check = []
    for student_i in student :
        check.append(int(student_i)%(moduler**length))
    else :
        if len(set(check)) == len(student) :
            print(length)
            break