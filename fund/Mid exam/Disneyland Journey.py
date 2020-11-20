needed = float(input())
months = int(input())
have = 0

for i in range(1, months + 1):
    if i % 2 != 0 and not i == 1:
        have *= 0.84
    if i % 4 == 0:
        have *= 1.25
    have += needed / 4

if have >= needed:
    print(f"Bravo! You can go to Disneyland and you will have {(have - needed):.2f}lv. for souvenirs.")
elif have < needed:
    print(f"Sorry. You need {(needed - have):.2f}lv. more.")