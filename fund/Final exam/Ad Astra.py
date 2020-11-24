import re

pattern = r'\|[A-Za-z ]+\|\d\d/\d\d/\d\d\|[0-9]+\||#[A-Za-z ]+#\d\d/\d\d/\d\d#[0-9]+#'
text = input()
match = re.findall(pattern, text)
calories = 0
for i in match:
    if "|" in i:
        token = i.split("|")
        calories += int(token[3])
    elif '#' in i:
        token = i.split("#")
        calories += int(token[3])
print(f"You have food to last you for: {calories//2000} days!")
for i in match:
    if "|" in i:
        token = i.split("|")
        print(f"Item: {token[1]}, Best before: {token[2]}, Nutrition: {token[3]}")
    elif '#' in i:
        token = i.split("#")
        print(f"Item: {token[1]}, Best before: {token[2]}, Nutrition: {token[3]}")