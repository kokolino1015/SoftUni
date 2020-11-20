shopping_list = input().split(" ")


def outofstock(stock):
    for i in range(len(shopping_list)):
        if shopping_list[i] == stock:
            shopping_list[i] = "None"


def required(stock, place):
    if -1 < place < len(shopping_list):
        shopping_list[place] = stock


def justincase(stock):
    shopping_list[-1] = stock


command = input()
while not command == "No Money":
    token = command.split(" ")
    action = token[0]
    product = token[1]
    if action == "OutOfStock":
        outofstock(product)
    elif action == "Required":
        index = token[2]
        required(product, int(index))
    elif action == "JustInCase":
        justincase(product)

    command = input()

while "None" in shopping_list:
    shopping_list.remove("None")
print(" ".join(shopping_list))
