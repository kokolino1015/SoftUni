import re

text = input()
pattern = r'(\*\*[A-z][a-z]+\*\*)|(::[A-Z][a-z]+::)'
match = re.findall(pattern, text)
digits = re.findall(r'\d', text)
list = []
for i in match:
    for j in range(len(i)):
        if len(i[j]) >= 7:
            list.append(i[j])
threshold = 1
for i in digits:
    threshold *= int(i)
print(f"Cool threshold: {threshold}")
print(f"{len(list)} emojis found in the text. The cool ones are:")
for i in list:
    cool = 0
    for j in range(2, len(i) - 2):
        cool += ord(i[j])
    if cool >= threshold:
        print(i)