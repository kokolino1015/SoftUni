def input_users(num):
    users = set()
    for _ in range(num):
        users.add(input())
    return users


def print_result(users):
    for user in users:
        print(user)


print_result(input_users(int(input())))
