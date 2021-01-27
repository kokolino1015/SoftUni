count = int(input())

students = {}

for _ in range(count):
    line = input().split()
    student = line[0]
    grade = float(line[1])
    if student not in students:
        students[student] = [float(grade)]
    else:
        students[student].append(float(grade))

for student, grade in students.items():
    string_of_grade = ''
    for g in grade:
        if len(str(g)) == 3:
            g = str(g) + "0"
        string_of_grade += str(g) + " "
    avg = sum(grade)/len(grade)

    print(f"{student} -> {string_of_grade}(avg: {avg:.2f})")
