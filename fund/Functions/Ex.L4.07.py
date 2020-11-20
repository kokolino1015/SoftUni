def perfect_number(number):
    a = []
    for i in range(1, number):
        if number % i == 0:
            a.append(i)
    if sum(a) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))