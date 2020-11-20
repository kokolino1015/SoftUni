import math

num_peoples = int(input())
capacity = int(input())
courses = 0
while True:
    if num_peoples <= 0:
        break
    if num_peoples >= capacity:
        courses += 1
        num_peoples -= capacity
    elif num_peoples < capacity:
        courses += 1
        break

print(courses)