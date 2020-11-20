numbers = input().split()
turn_ar = 1


def adding(turning):
    element = f"-{turning}a"
    if element not in numbers:
        middle = len(numbers) // 2
        numbers.insert(middle, element)
        numbers.insert(middle, element)


def removing(first_number, second_number):
    print(f"Congrats! You have found matching elements - {numbers[int(first_number)]}!")
    if first_number > second_number:
        numbers.pop(int(first_number))
        numbers.pop(int(second_number))
    else:
        numbers.pop(int(second_number))
        numbers.pop(int(first_number))


command = input()
while True:
    if command == 'end':
        break
    turn = command.split()
    first = int(turn[0])
    second = int(turn[1])
    if first == second or first < 0 or second < 0 or second >= len(numbers) or first >= len(numbers):
        adding(turn_ar)
        print("Invalid input! Adding additional elements to the board")
    else:
        if numbers[second] == numbers[first]:
            removing(first, second)
            if not numbers:
                break
        elif numbers[first] != numbers[second]:
            print("Try again!")
    command = input()
    turn_ar += 1

if not numbers:
    print(f"You have won in {turn_ar} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(numbers))
