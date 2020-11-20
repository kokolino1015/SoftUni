shuffles = int(input())
dictionary = {}

for i in range(shuffles):
    name = input()
    grade = float(input())
    if name not in dictionary:
        dictionary[name] = []
    dictionary[name].append(grade)

for key in dictionary:
    avr = len(dictionary[key])
    total = 0
    for i in dictionary[key]:
        total += float(i)
    dictionary[key] = total/avr

dictionary = sorted(dictionary.items(), key=lambda x: -(x[1]))

dictionary2 = {}

for key, value in dictionary:
    if float(value) < 4.50:
        continue
    else:
        dictionary2[key] = value


for key, value in dictionary2.items():
    print(f"{key} -> {float(value):.2f}")

