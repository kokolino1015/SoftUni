lines = input()
for i in range(len(lines)):
    if ":" == lines[i]:
        print(f":{lines[i + 1]}")