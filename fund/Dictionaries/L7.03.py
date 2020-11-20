products = {}
products_num = 0
quality = 0

command = input()
while command != "statistics":
    token = command.split(": ")
    key = token[0]
    product = int(token[1])
    if key in products:
        products[key] += product
        quality += product
    else:
        quality += product
        products[key] = product
        products_num += 1
    command = input()

print("Products in stock:")
for i in products:
    print(f"- {i}: {products[i]}")
print(f"Total Products: {products_num}")
print(f"Total Quantity: {quality}")
