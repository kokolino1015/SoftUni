words = input().split(" ")
word1 = words[0]
word2 = words[1]
total = 0

min_size = min(len(word1), len(word2))

for i in range(min_size):
    str1 = ord(word1[i])
    str2 = ord(word2[i])
    total += str1 * str2

bigger = ""
smaller = ""
if len(word1) > len(word2):
    bigger = word1
    smaller = word2
else:
    bigger = word2
    smaller = word1

for i in range(len(smaller), len(bigger)):
    total += ord(bigger[i])

print(total)
