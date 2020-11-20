items = input().split(", ")


def collect(item):
    if item not in items:
        items.append(item)


def drop(item):
    if item in items:
        items.remove(item)


def combine_items(old_item, new_item):
    if old_item in items:
        index = items.index(old_item)
        items.insert(index + 1, new_item)


def renew(item):
    if item in items:
        items.remove(item)
        items.append(item)


command = input()
while not command == "Craft!":
    token = command.split(" - ")
    action = token[0]
    if action == "Collect":
        collect(token[1])
    elif action == "Drop":
        drop(token[1])
    elif action == "Combine Items":
        tokens = token[1].split(":")
        combine_items(tokens[0], tokens[1])
    elif action == "Renew":
        renew(token[1])
    command = input()
print(", ".join(items))