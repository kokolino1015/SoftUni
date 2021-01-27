num = int(input())

numbers_dict = {}
for num in range(num):
    command = input().split(" ")
    if command[0] not in numbers_dict:
        numbers_dict[command[0]] = []
    numbers_dict[command[0]].append(float(command[1]))

for key, value in numbers_dict.items():
    string = ''
    for i in value:
        if len(str(i)) < 4:
            string += str(i) + '0 '
        else:
            string += str(i) + ' '
    avr = sum(value) / len(value)
    print(f"{key} -> {string}(avg: {avr:.2f})")
