from collections import deque
n = int(input())
petrol = deque([])
dist = deque([])
tank = 0
current_index = 0
next_station = 0

for i in range(n):
    add_petrol, add_distance = input().split()
    petrol.append(add_petrol)
    dist.append(add_distance)

petrol.append(petrol[0])
dist.append(dist[0])

while True:
    add_to_tank = int(petrol[next_station]) - int(dist[next_station])
    if tank + add_to_tank < 0:
        current_index += 1
        next_station = 0
        tank = 0
        petrol.popleft()
        petrol.append(petrol[0])
        dist.popleft()
        dist.append(dist[0])
        continue
    else:
        tank += add_to_tank
        next_station += 1
        if next_station == n:
            break

print(current_index)
