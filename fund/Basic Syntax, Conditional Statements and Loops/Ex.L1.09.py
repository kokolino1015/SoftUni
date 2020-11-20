budget = float(input())
flour = float(input())

eggs = 0.75 * flour
milk_for_1_liter = 0.25 * flour + flour

cozonacs_price = flour + eggs + milk_for_1_liter / 4

colored_eggs = 0
cozonac = 0

while True:
    if budget > cozonacs_price:
        budget -= cozonacs_price
        cozonac += 1
        colored_eggs += 3
        if cozonac % 3 == 0:
            colored_eggs -= cozonac - 2
    else:
        break

print(f"You made {cozonac} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")