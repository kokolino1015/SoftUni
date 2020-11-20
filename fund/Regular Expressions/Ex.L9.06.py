import re

list = []
f = r"www.[a-zA-Z0-9]+(-([a-zA-Z0-9]+))*\.[a-z]+(\.([a-z]+))*"
pattern = r"(www.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.[a-z]+(\.([a-z]+))*)"
text = input()
while True:
    if not text:
        break
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group(0))
    text = input()