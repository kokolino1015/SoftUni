def input_list(n):
    return [input() for _ in range(n)]


def arrived(command):
    result = []
    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    return result


def not_arrived(one, two):
    return set(one) - set(two)


def print_guests(list):
    list = sorted(list)
    print(len(list))
    [print(guest) for guest in list if guest[0].isdigit()]
    [print(guest) for guest in list if not guest[0].isdigit()]


list_of_peoples = input_list(int(input()))
arrived_guests = arrived("END")
guest = not_arrived(list_of_peoples, arrived_guests)
print_guests(guest)
