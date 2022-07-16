m, d = map(int, input().split())
flowDay = 0

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for x in range (0, m-1) :
    flowDay += month[x]

flowDay = (flowDay + d) % 7

print(week[flowDay])