def length(password):
    if len(password) < 6 or len(password) > 10:
        return "Password must be between 6 and 10 characters"


def digits(password):
    s = 0
    for i in password:
        if i.isdigit():
            s += 1
    if s < 2:
        return "Password must have at least 2 digits"


def characters(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return "Password must consist only of letters and digits"


def get_password():
    return [
        characters,
        digits,
        length
    ]


def solve(password):
    validators = get_password()
    validation_errors = []
    for validator in validators:
        result = validator(password)
        if result is not None:
            validation_errors.append(result)
    if len(validation_errors) == 0:
        return "Password is valid"
    else:
        return '\n'.join(validation_errors)


password = input()
result = solve(password)
print(result)