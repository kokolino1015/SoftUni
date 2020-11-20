dictionary_names = {}
dictionary_results = {}


def check(key, dict, points):
    if key in dict:
        value = dict[key]
        if points > value:
            value = points
            dict[key] = value
        else:
            dict[key] = value


def split(key, dict, points):
    if key not in dict:
        dict[key] = points


def tech(key, dict):
    if key not in dict:
        dict[key] = 0
    dict[key] += 1


line = input()
while line != "exam finished":
    if "banned" in line:
        token = line.split("-")
        user = token[0]
        ban = token[1]
        del dictionary_names[user]
    else:
        token = line.split("-")
        user = token[0]
        technology = token[1]
        points = int(token[2])
        split(user, dictionary_names, points)
        check(user, dictionary_names, points)
        tech(technology, dictionary_results)
    line = input()

dictionary_names = dict(sorted(dictionary_names.items(), key=lambda x: ((-x[1]), x[0])))
dictionary_results = dict(sorted(dictionary_results.items(), key=lambda x: ((-x[1]), x[0])))

print("Results:")
for k, v in dictionary_names.items():
    print(f"{k} | {v}")
print("Submissions:")
for k, v in dictionary_results.items():
    print(f"{k} - {v}")
