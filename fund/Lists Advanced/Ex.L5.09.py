houses = [int(x) for x in input().split("@")]
house = 0

command = input()
while True:
    if command == "Love!":
        break
    num = command.split(" ")
    house += int(num[1])
    if house >= len(houses):
        house = 0
    if houses[house] == 0:
        print(f"Place {house} already had Valentine's day.")
    else:
        houses[house] -= 2
        if houses[house] <= 0:
            print(f"Place {house} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {house}.")
failed = 0
for i in houses:
    if i > 0:
        failed += 1
if failed != 0:
    print(f"Cupid has failed {failed} places.")
elif failed == 0:
    print("Mission was successful.")