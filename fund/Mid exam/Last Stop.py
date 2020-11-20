paintings = input().split(" ")


def change(painting, changed):
    if painting in paintings:
        index = paintings.index(painting)
        paintings.pop(index)
        paintings.insert(index, changed)


def hide(painting):
    if painting in paintings:
        paintings.remove(painting)


def switch(painting1, painting2):
    if painting2 in paintings and painting1 in paintings:
        f_index = paintings.index(painting1)
        s_index = paintings.index(painting2)
        paintings[f_index], paintings[s_index] = paintings[s_index], paintings[f_index]


def insert(index, painting):
    if index + 1 in range(len(paintings)):
        paintings.insert(index + 1, painting)


command = input()
while not command == "END":
    token = command.split(" ")
    action = token[0]
    if action == "Change":
        change(token[1], token[2])
    elif action == "Hide":
        hide(token[1])
    elif action == "Switch":
        switch(token[1], token[2])
    elif action == "Insert":
        insert(int(token[1]), token[2])
    elif action == "Reverse":
        paintings.reverse()
    command = input()

print(" ".join(paintings))
