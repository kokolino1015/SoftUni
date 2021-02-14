text = input()
vowels = ["a", "e", "u", "o", "i"]

word = "".join([x for x in text if x not in vowels])
print(word)
