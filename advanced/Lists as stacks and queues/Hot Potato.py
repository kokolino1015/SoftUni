from collections import deque

person = input().split(' ')
queue = deque(person)
cycle = int(input())
i = 1

while len(queue) > 1:
    person = queue.popleft()

    if i == cycle:
        print(f'Removed {person}')
        i = 0
    else:
        queue.append(person)
    i += 1

print(f'Last is {queue.pop()}')
