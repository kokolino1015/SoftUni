items = [x for x in input().split(", ")]


def collect(item):
    if item in items:
        return
    items.append(item)


def drop(item):
    if item in items:
        items.remove(item)


def combine_items(item):
    res = item.split(":")
    if res[0] in items:
        place = 0
        for i in items:
            if i == res[0]:
                break
            place += 1
        items.insert(place + 1, res[1])


def renew(item):
    if item in items:
        items.remove(item)
        items.append(item)


def main(command):
    if "Renew" in command:
        token = command.split(" - ")
        item = token[1]
        renew(item)
    elif "Collect" in command:
        token = command.split(" - ")
        item = token[1]
        collect(item)
    elif "Drop" in command:
        token = command.split(" - ")
        item = token[1]
        drop(item)
    elif "Combine Items" in command:
        token = command.split(" - ")
        item = token[1]
        combine_items(item)


command = input()
while True:
    if command == "Craft!":
        break
    main(command)
    command = input()
print(", ".join(items))
