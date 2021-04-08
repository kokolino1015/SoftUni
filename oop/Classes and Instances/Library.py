class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
            if user.username in self.rented_books:
                del self.rented_books[user.username]
        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        username_for_change = [user for user in self.user_records if user.user_id == user_id]
        if username_for_change:
            if username_for_change[0].username == new_username:
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"
            username_for_change[0].username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            if user.username not in library.rented_books:
                library.rented_books[user.username] = {}
            library.rented_books[user.username].update({book_name:days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for data in library.rented_books.values():
            for book, day in data.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {day} days!'

    def return_book(self, author, book_name, library):
        if book_name in library.rented_books[user.username]:
            library.rented_books[user.username].pop(book_name)
            library.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"

    def info(self):
        return f'{";".join(sorted(self.books))}'

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
