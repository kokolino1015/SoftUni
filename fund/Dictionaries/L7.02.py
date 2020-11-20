elements = input().split(" ")
searching = input().split(" ")
bakery = {}
for product in range(0, len(elements), 2):
    key = elements[product]
    thing = elements[product + 1]
    if thing.isdigit():
        bakery[key] = int(thing)
    else:
        bakery[key] = thing

for product in searching:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
