string = input()


def take_odd(string):
    res = ""
    for i in range(len(string)):
        if i % 2 != 0:
            res += string[i]
    return res


def cut(string, index, length):
    list = []
    for i in string:
        list.append(i)
    start = int(index)
    end = start + int(length)
    del list[start:end]
    res = ""
    for i in list:
        res += i
    return res


def substitute(string, symbol, replace_symbol):
    if symbol not in string:
        print("Nothing to replace!")
    elif symbol in string:
        string = string.replace(symbol, replace_symbol)
        print(string)
    return string


command = input()
while not command == "Done":
    token = command.split(" ")
    if token[0] == "TakeOdd":
        string = take_odd(string)
        print(string)
    elif token[0] == "Cut":
        string = cut(string, token[1], token[2])
        print(string)
    elif token[0] == "Substitute":
        string = substitute(string, token[1], token[2])
    command = input()

print(f'Your password is: {string}')
