students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort()

lowest = 100

for i in range(len(students)):
    if students[i][1] < lowest:
        lowest = students[i][1]

for i in range(len(students) - 1, -1, -1):
    if students[i][1] == lowest:
        students.pop(i)

lowest = 100

for i in range(len(students)):
    if students[i][1] < lowest:
        lowest = students[i][1]

for i in range(len(students)):
    if students[i][1] == lowest:
        print(students[i][0])