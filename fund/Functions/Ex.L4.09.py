number = int(input())
r = int(input())


def factorial_division(number, r):
    product = 1
    for i in range(number, r, -1):
        product *= i
    return f"{product:.2f}"


print(factorial_division(number, r))
