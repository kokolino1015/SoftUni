things = input().split("|")
budget = float(input())

word = "Clothes"
word2 = "Shoes"
word3 = "Accessories"

total = 0
old_sum = 0
list = []

profit = 0

for i in things:
    tokens = i.split("->")
    name = tokens[0]
    cost = float(tokens[1])
    if word in name:
        if cost <= 50.00:
            if budget >= cost:
                budget -= cost
                old_sum += cost
                cost *= 1.4
                list.append(cost)
                profit += cost
                total += cost
            else:
                continue
        else:
            continue
    elif word2 in name:
        if cost <= 35.00:
            if budget >= cost:
                budget -= cost
                old_sum += cost
                cost *= 1.4
                list.append(cost)
                profit += cost
                total += cost
            else:
                continue
        else:
            continue
    elif word3 in name:
        if cost <= 20.50:
            if budget >= cost:
                budget -= cost
                old_sum += cost
                cost *= 1.4
                list.append(cost)
                profit += cost
                total += cost
            else:
                continue
        else:
            continue


for i in list:
    print(f"{i:.2f}", end=" ")

print()

profit -= old_sum
total += budget

if total >= 150:
    print(f"Profit: {profit:.2f}")
    print("Hello, France!")
elif total < 150:
    print(f"Profit: {profit :.2f}")
    print("Time to go.")