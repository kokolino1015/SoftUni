quantity = int(input())
days = int(input())

cost = 0
spirit = 0

ornament_set = 2
skirt = 5
tree = 3
light = 15

for i in range(1, days + 1):
    if i % 15 == 0:
        spirit += 30
    if i % 11 == 0:
        quantity += 2
    if i % 10 == 0:
        spirit -= 20
        cost += skirt + tree + light
        if i == days:
            spirit -= 30
    if i % 5 == 0:
        cost += light * quantity
        spirit += 17
    if i % 3 == 0:
        cost += (skirt + tree) * quantity
        spirit += 13
    if i % 2 == 0:
        cost += ornament_set * quantity
        spirit += 5

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")