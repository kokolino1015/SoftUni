import math

company = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        company -= 2

    if i % 15 == 0:
        company += 5
        coins -= 2 * company

    coins += 50 - (2 * company)

    if i % 3 == 0:
        coins -= 3 * company

    if i % 5 == 0:
        coins += 20 * company


coins_rent = math.floor(coins // company)
print(f"{company} companions received {coins_rent} coins each.")