from collections import deque

food = int(input())
order = input().split(" ")
orders = deque()
max_client = 0
for i in order:
    if max_client < int(i):
        max_client = int(i)
    orders.append(int(i))
print(max_client)

while True:
    if len(orders) < 1:
        break
    if int(orders[0]) <= food:
        food -= int(orders[0])
        orders.popleft()
    else:
        break

orders = [str(x) for x in orders]
if orders:
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete")
