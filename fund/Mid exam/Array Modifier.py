def swap(index1, index2):
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    return numbers


def multiply(index1, index2):
    num = numbers[index1]
    num *= numbers[index2]
    numbers[index1] = num
    return numbers


def decrease():
    index = 0
    for number in numbers:
        numbers[index] -= 1
        index += 1
    return numbers


numbers = input().split(" ")
numbers = [int(number) for number in numbers]

command = input()

while command != 'end':
    token = command.split(" ")
    func = token[0]
    if func == "swap":
        element1 = int(token[1])
        element2 = int(token[2])
        swap(element1, element2)
    elif func == "decrease":
        decrease()
    elif func == "multiply":
        element1 = int(token[1])
        element2 = int(token[2])
        multiply(element1, element2)
    command = input()

numbers = [str(number) for number in numbers]

print(", ".join(numbers))