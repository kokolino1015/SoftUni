text = input().split(", ")

dictionary = {word: ord(word) for word in text}
print(dictionary)
