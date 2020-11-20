list_symbols = []
line = input()
master = ""
result = ""
for i in range(len(line)):
    ch = line[i]
    if ch.isdigit():
        result1 = ch
        if i + 1 < len(line) and line[i + 1].isdigit():
            result1 += line[i + 1]
        master += (f"{result}" * int(result1))
        result = ""
    else:
        ch = ch.upper()
        result += ch

print(f"Unique symbols used: {len(set(master))}")
print(master)
