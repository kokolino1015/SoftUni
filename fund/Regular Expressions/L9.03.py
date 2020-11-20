import re

text = input()
pattern = '\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b'
match = re.findall(pattern, text)
for math in match:
    print(f"Day: {math[0]}, Month: {math[2]}, Year: {math[3]}")
