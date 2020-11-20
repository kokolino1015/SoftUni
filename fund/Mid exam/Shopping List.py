shopping_list = input().split("!")


def urgent(item):
    if item in shopping_list:
        return
    shopping_list.insert(0, item)


def unnecessary(item):
    if item in shopping_list:
        shopping_list.remove(item)


def correct(old_item, new_item):
    if old_item in shopping_list:
        if new_item not in shopping_list:
            place = 0
            for i in shopping_list:
                if i == old_item:
                    break
                place += 1
            shopping_list.insert(place, new_item)
            shopping_list.remove(old_item)


def rearranged(item):
    if item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)


command = input()
while True:
    if command == "Go Shopping!":
        break
    token = command.split(" ")
    if token[0] == "Urgent":
        urgent(token[1])
    elif token[0] == "Unnecessary":
        unnecessary(token[1])
    elif token[0] == "Correct":
        correct(token[1], token[2])
    elif token[0] == "Rearrange":
        rearranged(token[1])
    command = input()

print(", ".join(shopping_list))