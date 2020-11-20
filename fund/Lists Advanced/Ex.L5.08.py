list = [int(x) for x in input().split(' ')]


def shoot(place, strength):
    if 0 <= place < len(list):
        move = list[place]
        move -= strength
        list[place] = move
        if list[place] <= 0:
            list.remove(list[place])


def strike(place, radius):
    start = place - radius
    end = place + radius
    if start >= 0 and end < len(list):
        del list[start: end + 1]
    else:
        print("Strike missed!")


def add(index, power):
    if 0 <= index < len(list):
        list.insert(index, power)
    else:
        print("Invalid placement!")


def main(command):
    if "Shoot" in command:
        command = command.split(" ")
        index = int(command[1])
        power = int(command[2])
        shoot(index, power)
    elif "Add" in command:
        command = command.split(" ")
        index = int(command[1])
        power = int(command[2])
        add(index, power)
    elif "Strike" in command:
        command = command.split(" ")
        index = int(command[1])
        power = int(command[2])
        strike(index, power)


text = input()
while True:
    if text == "End":
        break
    main(text)
    text = input()

index = 1
list = [str(x) for x in list]
print("|".join(list))
