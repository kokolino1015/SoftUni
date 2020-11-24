text = input()


def move(num_of_let, text2):
    list = []
    for i in text2:
        list.append(i)
    let = list[0:num_of_let]
    text = text2.replace("".join(let), "")
    text += "".join(let)
    return text


def insert(index, value, text2):
    list = []
    for i in text2:
        list.append(i)
    list.insert(index, value)
    text = "".join(list)
    return text


def changeall(substring, replacement, text2):
    text = text2.replace(substring, replacement)
    return text


def solve():
    global text
    command = input()
    while not command == "Decode":
        token = command.split("|")
        if token[0] == 'Move':
            res = move(int(token[1]), text)
            text = res
        elif token[0] == 'Insert':
            res = insert(int(token[1]), token[2], text)
            text = res
        elif token[0] == 'ChangeAll':
            res = changeall(token[1], token[2], text)
            text = res
        command = input()
    print(f"The decrypted message is: {text}")


solve()
