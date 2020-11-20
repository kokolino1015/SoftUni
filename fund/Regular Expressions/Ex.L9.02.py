import re

text = input()
pattern = r"\b(_[a-zA-Z0-9]+)\b"
matches = re.findall(pattern, text)
index = 1
for i in matches:
    word = i
    if index == len(matches):
        print(word[1:])
        break
    print(word[1:], end=",")
    index += 1
