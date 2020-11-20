import re

total = 0
text = input()
pattern = r">>([A-Za-z]+)<<(\d+(\.[\d]+)*)!(\d+)"
print("Bought furniture:")
while True:
    if text == "Purchase":
        break
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group(1))
        total += float(match.group(2)) * int(match.group(4))
    text = input()
print(f"Total money spend: {total:.2f}")