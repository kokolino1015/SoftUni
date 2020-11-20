word = input()
word2 = input()
index = 0
g = list(map(str, word))
for i in word2:
    g.pop(index)
    g.insert(index, i)
    if word[index] != g[index]:
        for j in g:
            print(j, end="")
        print()
    index += 1
