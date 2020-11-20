import re
name = input()
pattern = r'(\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})'
match = re.findall(pattern, name)
print(", ".join(match))