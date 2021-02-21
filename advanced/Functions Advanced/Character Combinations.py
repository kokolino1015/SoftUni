def permutation(word, index=0):
    if index == len(word):
        print(''.join(word))
        return

    for i in range(index, len(word)):
        word[index], word[i] = word[i], word[index]
        permutation(word, index + 1)
        word[index], word[i] = word[i], word[index]


text = list(input())
permutation(text)
