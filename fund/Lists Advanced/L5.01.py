num = int(input())
list_of_peoples = []

for i in range(num):
    list_of_peoples .append(0)

changes = input().split(" ")
while changes[0] != "End":
    if changes[0] == "add":
        list_of_peoples[num - 1] += int(changes[1])
    elif changes[0] == "insert":
        list_of_peoples[int(changes[1])] += int(changes[2])
    elif changes[0] == "leave":
        list_of_peoples[int(changes[1])] -= int(changes[2])
    changes = input().split(" ")

print(list_of_peoples)