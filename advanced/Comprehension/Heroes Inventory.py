def get_heroes():
    heroes = {name: {"item": [], "cost": []} for name in input().split(", ")}
    return heroes


def collect_all_of_us(heroes):
    while True:
        command = input()
        if command == "End":
            break
        hero, item, cost = command.split("-")
        if item not in heroes[hero]["item"]:
            heroes[hero]["item"].append(item)
            heroes[hero]["cost"].append(int(cost))
    return heroes


def print_heroes(heroes):
    print(*[f"{key} -> Items: {len(value['item'])}, Cost: {sum(value['cost'])}" for key, value in heroes.items()], sep="\n")


print_heroes(collect_all_of_us(get_heroes()))
