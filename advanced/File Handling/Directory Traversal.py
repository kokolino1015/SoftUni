import os

_, _, files = next(os.walk(input()))
dict = {}
for i in files:
    n = i.split('.')[1]
    if n not in dict:
        dict[n] = []
    dict[n].append(i)

new_dict = sorted(dict.items(), key=lambda x: x[0])
result = ''
for i, j in new_dict:
    result += f'.{i}\n'
    for p in j:
        result += f"- - - {p}.{i}\n"
desktop = os.path.normpath(os.path.expanduser('~\\Desktop\\report.txt'))

with open(os.path.expanduser('~\\Desktop\\report.txt'), 'w') as file:
    file.write(result)
