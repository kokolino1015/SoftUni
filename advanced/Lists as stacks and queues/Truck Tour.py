from collections import deque
n = int(input())
queue = deque([])

for _ in range(n):
    i = input().split()
    queue.append([int(i[0]), int(i[1])])

for i in range(n):
    go_through_all = 0
    fuel_tank = 0
    for gas_pumps in queue:
        fuel, distance = gas_pumps[0], gas_pumps[1]
        fuel_tank += fuel
        if fuel_tank < distance:
            break
        fuel_tank -= distance
        go_through_all += 1

    if go_through_all == len(queue):
        print(i)
        break
    queue.rotate(-1)
    
