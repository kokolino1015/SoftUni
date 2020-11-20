shops = input().split(" ")


def include(shop):
    shops.append(shop)


def visit(start_point, index):
    index = int(index)
    if index <= len(shops):
        if start_point == "first":
            start = 0
            end = index
            del shops[start:end]
        elif start_point == "last":
            index = index - index * 2
            start = index
            del shops[start:]


def prefer(first, second):
    first = int(first)
    second = int(second)
    if first in range(len(shops)) and second in range(len(shops)):
        shops[first], shops[second] = shops[second], shops[first]


def place(shop, index):
    index = int(index)
    if 0 <= index + 1 < len(shops):
        shops.insert(index + 1, shop)


num = int(input())
for i in range(num):
    command = input()
    token = command.split(" ")
    action = token[0]
    if action == "Include":
        include(token[1])
    elif action == "Visit":
        visit(token[1], token[2])
    elif action == "Prefer":
        prefer(token[1], token[2])
    elif action == "Place":
        place(token[1], token[2])

print("Shops left:")
print(" ".join(shops))
