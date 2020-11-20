list_of_peoples = [0] * 10

changes = input()
while changes != "End":
    tokens = changes.split("-")
    token = int(tokens[0])
    insert = tokens[1]
    list_of_peoples.pop(token - 1)
    list_of_peoples.insert(token - 1, insert)
    changes = input()
while 0 in list_of_peoples:
    list_of_peoples.remove(0)

print(list_of_peoples)
