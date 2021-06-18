import re

file = open('text.txt')
index = 1

for i in file.readlines():
    sentence = [j for j in i]
    sentence.pop()
    match_1 = re.findall(r"[a-zA-Z]", i)
    match_2 = re.findall(r"[\.\-,\?!\'\"]", i)
    print(f'Line {index}: {"".join(sentence)} ({len(match_1)}) ({len(match_2)})')
    index += 1
