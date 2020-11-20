import math

students = int(input())
lectures = int(input())
initial_bonus = int(input())
best_attend = -999999
if lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for i in range(students):
        attend = int(input())
        if attend > best_attend:
            best_attend = attend

    max_bonus = best_attend / lectures * (5 + initial_bonus)
    print(f"Max Bonus: {math.ceil(max_bonus)}.")
    print(f"The student has attended {best_attend} lectures.")