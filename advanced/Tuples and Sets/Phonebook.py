def input_contacts():
    persons = []
    contacts = {}
    while True:
        command = input()
        if command.isdigit():
            for el in range(int(command)):
                persons.append(input())
            break
        name, num = command.split("-")
        contacts[name] = num
    return persons, contacts


def search_contacts(phone, names):
    for i in phone:
        if i in names:
            print(f"{i} -> {names[i]}")
        else:
            print(f"Contact {i} does not exist.")


phone_books, names = input_contacts()
search_contacts(phone_books, names)
