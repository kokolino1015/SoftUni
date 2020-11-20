books = input().split("&")


def add(book):
    if book not in books:
        books.insert(0, book)


def take(book):
    if book in books:
        books.remove(book)


def swap(book1, book2):
    if book1 in books and book2 in books:
        book1_index = books.index(book1)
        book2_index = books.index(book2)
        books[book1_index], books[book2_index] = books[book2_index], books[book1_index]


def insert(book):
    books.append(book)


def check(index):
    if index in range(len(books)):
        print(books[index])


command = input()
while not command == "Done":
    token = command.split(" | ")
    action = token[0]
    if action == "Add Book":
        add(token[1])
    elif action == "Take Book":
        take(token[1])
    elif action == "Swap Books":
        swap(token[1], token[2])
    elif action == "Insert Book":
        insert(token[1])
    elif action == "Check Book":
        check(int(token[1]))
    command = input()

print(", ".join(books))
