word = input()

for i in range(len(word) - 1, -1, -1):
    s = word[i]
    print(s, end="")