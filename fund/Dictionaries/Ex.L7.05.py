entries = int(input())

dictionary = {}
for i in range(entries):
    register = input().split(" ")
    type = register[0]
    key = register[1]
    if type == "register":
        if key not in dictionary:
            dictionary[key] = register[2]
            print(f"{key} registered {dictionary[key]} successfully")
        elif key in dictionary:
            print(f"ERROR: already registered with plate number {dictionary[key]}")
    elif type == "unregister":
        if key not in dictionary:
            print(f"ERROR: user {key} not found")
        elif key in dictionary:
            print(f"{key} unregistered successfully")
            del dictionary[key]

for i in dictionary:
    print(f"{i} => {dictionary[i]}")