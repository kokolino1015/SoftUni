from custom_exceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError

VALID_DOMAINS = ("com", "bg", "org", "net")


def valid(email):
    try:
        name, extension = email.split('@')
    except KeyError:
        raise MustContainAtSymbolError("Email must contain @")
    try:
        name, extension = email.split('.')
    except KeyError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if not extension not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")
    return True


while True:
    email = input()
    if valid(email):
        print("Email is valid")
