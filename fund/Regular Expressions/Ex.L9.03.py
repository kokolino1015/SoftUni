import re

text = input()
searched = input()
pattern = fr"\b{searched}\b"
match = re.findall(pattern, text, re.IGNORECASE)
print(len(match))