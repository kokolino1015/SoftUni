first_string = input()
second_string = input()
new_str = first_string
l = len(first_string)

for i in range(0, l):
    if new_str[i] == second_string[i]:
        continue
    else:
        new_str = second_string[0:(i + 1)] + first_string[(i + 1):l]
        print(new_str)
