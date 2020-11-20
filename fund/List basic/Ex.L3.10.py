orders = input().split("|")
energy = 100
coins = 100
is_ended = False

word = "rest"
word2 = "order"

counter = 0

for i in orders:
    counter += 1

for f in orders:
    tokens = f.split("-")
    name = tokens[0]
    cost = int(tokens[1])
    if word in f:
        energy += cost
        if energy >= 100:
            print(f"You gained 0 energy.")
            print(f"Current energy: 100.")
            energy = 100
        else:
            print(f"You gained {cost} energy.")
            print(f"Current energy: {energy}.")
    elif word2 in name:
        if energy < 30:
            print("You had to rest!")
            energy += 50
            continue
        energy -= 30
        coins += cost
        print(f"You earned {cost} coins.")
    else:
        if coins <= cost:
            print(f"Closed! Cannot afford {name}.")
            is_ended = True
            break
        coins -= cost
        print(f"You bought {name}.")

if coins > 0 and not is_ended:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
