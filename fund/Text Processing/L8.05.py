line = input()
", ".join(line)
result1 = ""
result2 = ""
result3 = ""
for i in line:
    if i.isdigit():
        result1 += i
    elif i.isalpha():
        result2 += i
    else:
        result3 += i

print(result1)
print(result2)
print(result3)