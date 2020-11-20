sentence = input().split(" ")


def delete(index):
    if index + 1 in range(len(sentence)):
        sentence.remove(sentence[index + 1])


def swap(word, word2):
    if word2 in sentence and word in sentence:
        word_index = sentence.index(word)
        word2_index = sentence.index(word2)
        sentence[word_index], sentence[word2_index] = sentence[word2_index], sentence[word_index]


def put(word, index):
    if 0 <= index - 1 <= len(sentence):
        sentence.insert(index - 1, word)


def sort():
    sentence.sort(reverse=True)


def replace(word, word2):
    if word2 in sentence:
        word2_index = sentence.index(word2)
        sentence[word2_index] = word


command = input()
while not command == "Stop":
    token = command.split(" ")
    action = token[0]

    if action == "Swap":
        swap(token[1], token[2])

    elif action == "Replace":
        replace(token[1], token[2])

    elif action == "Delete":
        delete(int(token[1]))

    elif action == "Put":
        put(token[1], int(token[2]))

    elif action == "Sort":
        sort()

    command = input()

print(" ".join(sentence))
