first_employers = int(input())
second_employer = int(input())
third_employer = int(input())
peoples = int(input())
hours = 0

while peoples > 0:
    hours += 1
    if hours % 4 == 0:
        pass
    else:
        per_hour = first_employers + second_employer + third_employer
        peoples -= per_hour


print(f"Time needed: {hours}h.")