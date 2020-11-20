def potion(health, get):
    if health + get >= 100:
        hp = 100 - health
        print(f"You healed for {hp} hp.")
        health = 100
    elif health + get < 100:
        print(f"You healed for {get} hp.")
        health += get
    print(f"Current health: {health} hp.")
    return health


def kill(health, damage, name):
    if health > damage:
        health -= damage
        print(f"You slayed {name}.")
        return health
    elif health <= damage:
        health = 0
        return health


rooms = input().split("|")
is_alive = True
bitcoins = 0
health = 100
room = 0

for i in rooms:
    room += 1
    token = i.split(" ")
    action = token[0]
    if action == "potion":
        res = potion(health, int(token[1]))
        health = res
    elif action == "chest":
        bitcoins += int(token[1])
        print(f"You found {int(token[1])} bitcoins.")
    else:
        res = kill(health, int(token[1]), token[0])
        health = res
        if health == 0:
            is_alive = False

    if not is_alive:
        print(f"You died! Killed by {token[0]}.")
        break

if is_alive:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
else:
    print(f"Best room: {room}")
