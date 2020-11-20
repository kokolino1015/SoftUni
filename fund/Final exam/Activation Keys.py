letters = input()
list = []
for i in range(len(letters)):
    list.append(letters[i])


def slice(start, end):
    del list[start:end]
    print("".join(list))


def flip(type, start, end):
    if type == "Upper":
        for i in range(len(list)):
            if start <= i < end:
                letter = list[i]
                list[i] = letter.upper()
    elif type == "Lower":
        for i in range(len(list)):
            if start <= i < end:
                letter = list[i]
                list[i] = letter.lower()
    print("".join(list))


def contain(word):
    if word in "".join(list):
        print(f"{''.join(list)} contains {word}")
    elif word not in "".join(list):
        print("Substring not found!")


command = input()
while not command == "Generate":
    token = command.split(">>>")
    if token[0] == "Contains":
        contain(token[1])
    elif token[0] == "Flip":
        flip(token[1], int(token[2]), int(token[3]))
    elif token[0] == "Slice":
        slice(int(token[1]), int(token[2]))
    command = input()

print(f"Your activation key is: {''.join(list)}")