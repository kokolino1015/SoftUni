lost_fight = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
b_h = 0
b_s = 0
b_sh = 0
b_a = 0
for i in range(1, lost_fight + 1):
    if i % 2 == 0:
        b_h += 1
    if i % 3 == 0:
        b_s += 1
    if i % 6 == 0:
        b_sh += 1
    if i % 12 == 0:
        b_a += 1

total = b_h * helmet + b_s * sword + b_sh * shield + b_a * armor
print(f"Gladiator expenses: {total:.2f} aureus")
