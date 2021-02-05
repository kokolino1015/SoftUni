def get_input():
    num = int(input())
    matrix = []
    for i in range(num):
        word = input()
        matrix.append(word)
    return (num, matrix)


def result(data):
    result = ""
    searching_element = input()
    for i in range(len(data[1])):
        word = data[1][i]
        if searching_element in word:
            element = word.index(searching_element)
            result = (i, element)
            break
    if result:
        print(result)
    else:
        print(f'{searching_element} does not occur in the matrix')

result(get_input())
