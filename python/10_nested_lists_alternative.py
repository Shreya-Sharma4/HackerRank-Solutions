students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set(score for name, score in students))
second_lowest = scores[1]

names = []

for name, score in students:
    if score == second_lowest:
        names.append(name)

names.sort()

for name in names:
    print(name)