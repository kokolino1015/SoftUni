explosion = input()
result = ""

strength = 0

for i in range(0, len(explosion)):
    ch = explosion[i]
    if ch == ">":
        strength += int(explosion[i + 1])
        result += ch
    elif strength != 0:
        strength -= 1
    else:
        result += ch

print(result)
