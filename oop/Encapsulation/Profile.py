class Profile:
    def __init__(self, username, password):
        self.username = self.set_name(username)
        self.password = self.set_password(password)

    def set_name(self, name):
        if 5 <= len(name) <= 15:
            return name
        raise ValueError("The username must be between 5 and 15 characters.")

    def set_password(self, password):
        numbers = '1234567890'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if len(password) >= 8:
            digits = [x for x in password if x in numbers]
            if digits:
                upper_case = [x for x in password if x in upper]
                if upper_case:
                    return password
                raise ValueError(
                    "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
