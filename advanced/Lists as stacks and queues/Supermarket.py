from collections import deque

queue = deque()
command = input()
while True:
    if command == "Paid":
        while queue:
            print(queue.popleft())
    elif command == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)
    command = input()
