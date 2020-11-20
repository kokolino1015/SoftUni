letters = input()
checker = f"{letters}0"
result = ""
for i in range(len(checker)):
    if i == len(checker) - 2:
        result += checker[i]
        break
    elif checker[i] == checker[i + 1]:
        continue
    elif checker[i] != checker[i + 1]:
        result += checker[i]
print(result)