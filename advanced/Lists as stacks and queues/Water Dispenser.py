from collections import deque

dispenser = int(input())
queue = deque()
is_started = False
command = input()
while command != "End":
    if command == "Start":
        is_started = True
    else:
        if not is_started:
            queue.append(command)
        elif is_started:
            if "refill" in command:
                token = command.split(' ')
                dispenser += int(token[1])
            else:
                if dispenser >= int(command):
                    dispenser -= int(command)
                    print(f"{queue.popleft()} got water")
                else:
                    print(f"{queue.popleft()} must wait")
    command = input()
print(f"{dispenser} liters left")
