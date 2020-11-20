targets = [int(x) for x in input().split("|")]
points = 0


def shoot_left(starting_point, ending_point):
    gain_points = 0

    index = (starting_point - ending_point) % len(targets)

    if targets[index] >= 5:
        targets[index] -= 5
        gain_points += 5

    else:
        gain_points += targets[index]
        targets[index] = 0

    return gain_points


def shot_right(starting_point, ending_point):
    gain_points = 0

    index = (starting_point + ending_point) % len(targets)

    if targets[index] >= 5:
        targets[index] -= 5
        gain_points += 5

    else:
        gain_points += targets[index]
        targets[index] = 0
    return gain_points


command = input()

while not command == 'Game over':
    token = command.split(" ")
    if token[0] == "Shoot":
        action = token[1].split("@")
        side = action[0]
        start = int(action[1])
        end = int(action[2])
        if start in range(len(targets)):
            if side == "Left":
                points += int(shoot_left(start, end))
            elif side == "Right":
                points += int(shot_right(start, end))
    elif token[0] == "Reverse":
        targets.reverse()
    command = input()

print(" - ".join(map(str, targets)))
print(f"Iskren finished the archery tournament with {points} points!")