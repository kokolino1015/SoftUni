elements = input().split(" ")
brakets = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    thing = elements[i + 1]
    if thing.isdigit():
        brakets[key] = int(thing)
    else:
        brakets[key] = thing
print(brakets)