z = 1

while True :
    cnt = int(input())
    if cnt == 0 :
        break
    else :
        student = []
        get = []
        for x in range(cnt) :
            student.append(input())
        for x in range(2 * cnt - 1) :
            check = int(input().split()[0])
            if check in get :
                get.remove(int(check))
            else :
                get.append(int(check))
        else :
            print(f"{z} {student[int(get[0])-1]}")
            z += 1