n = int(input())

student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

for student in student_marks:
    if student == query_name:
        average = sum(student_marks[student]) / len(student_marks[student])
        print(f"{average:.2f}")