def get_heroes():
    resources = {name: {"item": [], "quantity": [], "quality": []} for name in input().split(", ")}
    return resources


def collect_all_of_us(resources):
    for i in range(int(input())):
        command = input()
        material, item, specs = command.split(" - ")
        quantity, quality = specs.split(";")
        q, qty = quantity.split(":")
        qe, qte = quality.split(":")
        if item not in resources[material]["item"]:
            resources[material]["item"].append(item)
            resources[material]["quantity"].append(int(qty))
            resources[material]["quality"].append(int(qte))
    return resources


def print_result(resources):
    quantity = sum([sum(val['quantity']) for val in resources.values()])
    quality = (sum([sum(value["quality"]) for key, value in resources.items()]) / len(resources))
    print(f"Count of items: {quantity}")
    print(f"Average quality: {quality:.2f}")
    print(*[f"{key} -> {', '.join(value['item'])}" for key, value in resources.items()], sep="\n")


print_result(collect_all_of_us(get_heroes()))
