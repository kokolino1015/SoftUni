words = input().split(" ")
searched_palindrome = input()
palindrome = []
for i in words:
    word = i
    word2 = "".join(reversed(word))
    if word2 == i:
        palindrome.append(i)
print(palindrome)
index = 0
while searched_palindrome in palindrome:
    palindrome.remove(searched_palindrome)
    index += 1
print(f"Found palindrome {index} times")