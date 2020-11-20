targets = [int(x) for x in input().split(" ")]


def add(index, points):
    if index in range(len(targets)):
        targets.insert(index, points)
    else:
        print("Invalid placement!")


def shoot(index, power):
    if index in range(len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def strike(index, radius):
    start = index - radius
    end = index + radius
    if start >= 0 and end + 1 < len(targets):
        del targets[start:end + 1]
    else:
        print("Strike missed!")


command = input()
while not command == "End":
    token = command.split(" ")
    if token[0] == "Shoot":
        shoot(int(token[1]), int(token[2]))
    elif token[0] == "Strike":
        strike(int(token[1]), int(token[2]))
    elif token[0] == "Add":
        add(int(token[1]), int(token[2]))
    command = input()

targets = [str(x) for x in targets]
print("|".join(targets))