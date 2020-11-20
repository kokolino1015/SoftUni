import re

text = input()
user_pattern = r"( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*"
host_pattern = r"[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"
pattern = fr"{user_pattern}@{host_pattern}"
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(0))
