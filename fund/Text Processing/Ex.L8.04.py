words = input().split(" ")
result = ""
for word in words:
    for index in range(len(word)):
        key = ord(word[index])
        result += chr(key + 3)
    if word == words[-1]:
        break
    result += "#"

print(result)