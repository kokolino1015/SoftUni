dictionary = {}
line = input()
while line != "end":
    key = line
    value = ""
    for i in reversed(line):
        value += i
    dictionary[key] = value
    line = input()

for k, v in dictionary.items():
    print(f"{k} = {v}")