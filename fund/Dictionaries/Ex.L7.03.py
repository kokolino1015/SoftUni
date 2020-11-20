def validation(dictinories, key, value):
    if key not in dictionary2:
        dictionary2[key] = 0
    dictionary2[key] += value


def print_dic(dictionaries, template):
    for k, v in dictionaries:
        print(template.format(k, v))


dictionary = {"fragments": 0, "motes": 0, "shards": 0}
dictionary2 = {}
is_running = False
while not is_running:
    items = input().split(" ")
    for word in range(0, len(items) - 1, 2):
        value = int(items[word])
        key = items[word + 1].lower()
        if key in dictionary:
            dictionary[key] += value
            if dictionary[key] >= 250:
                if key == "shards":
                    print("Shadowmourne obtained!")
                    dictionary[key] -= 250
                elif key == "motes":
                    print("Dragonwrath obtained!")
                    dictionary[key] -= 250
                elif key == "fragments":
                    print("Valanyr obtained!")
                    dictionary[key] -= 250
                is_running = True
                break
        else:
            validation(dictionary2, key, value)


dictionary = sorted(dictionary.items(), key=lambda el: (-el[1], el[0]))
print_dic(dictionary, "{}: {}")
dictionary2 = sorted(dictionary2.items())
print_dic(dictionary2, "{}: {}")
