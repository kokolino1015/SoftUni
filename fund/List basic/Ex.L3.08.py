fires = input().split("#")
water = int(input())

word = "High"
word2 = "Medium"
word3 = "Low"

total = 0

print("Cells:")

for i in fires:
    tokens = i.split(" = ")
    name = tokens[0]
    cost = int(tokens[1])

    if water < cost:
        continue

    if word in name:
        if cost <= water:
            if 81 <= cost <= 125:
                water -= cost
                total += cost
                print(f" - {cost}")
            else:
                continue
        else:
            continue
    elif word2 in name:
        if cost <= water:
            if 51 <= cost <= 80:
                water -= cost
                total += cost
                print(f" - {cost}")
            else:
                continue
        else:
            continue
    elif word3 in name:
        if cost <= water:
            if 1 <= cost <= 50:
                water -= cost
                total += cost
                print(f" - {cost}")
            else:
                continue
        else:
            continue

print(f"Effort: {(total / 4):.2f}")
print(f"Total Fire: {total}")
