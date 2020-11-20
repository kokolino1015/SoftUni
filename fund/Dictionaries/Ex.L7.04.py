dictionary = {}
is_running = True

while is_running:
    items = input().split(" ")
    if items[0] == "buy":
        is_running = False
        break
    key = items[0]
    if key not in dictionary:
        value = float(items[1])
        quanity = int(items[2])
        dictionary[key] = value, quanity
    elif key in dictionary:
        new_price = float(items[1])
        quanitys = int(items[2])
        price = new_price
        quanity = dictionary[key]
        quanitysss = int(quanity[1])
        quanitysss += quanitys
        dictionary[key] = price, quanitysss


for i in dictionary:
    value = dictionary[i]
    price = float(value[0])
    quanity = int(value[1])
    value = price * quanity
    dictionary[i] = value
    print(f"{i} -> {dictionary[i]:.2f}")
