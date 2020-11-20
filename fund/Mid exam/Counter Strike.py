energy = int(input())
is_won = True
won_battles = 0

while True:
    command = input()
    if command == "End of battle":
        break
    else:
        command = int(command)
    if energy >= command:
        energy -= command
        won_battles += 1
    else:
        is_won = False
        break
    if won_battles % 3 == 0:
        energy += won_battles

if is_won:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
elif not is_won:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
