import re
text = input()
pattern = r"=([A-Z]([A-Za-z]+){2})=|/([A-Z]([A-Za-z]+){2})/"
match = re.finditer(pattern, text)
list = []
for i in match:
    list.append(i.group(0))
list2 = []
for i in range(len(list)):
    v = list[i]
    if "=" in v:
        v = v.replace("=", "")
    elif "/" in v:
        v = v.replace("/", "")
    list2.append(v)
print(f"Destinations: {', '.join(list2)}")
travel_points = 0
for i in list2:
    for j in i:
        travel_points += 1
print(f"Travel Points: {travel_points}")

