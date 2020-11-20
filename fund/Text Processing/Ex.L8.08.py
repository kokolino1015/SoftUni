def summing(first, digit, last):
    if first.isupper():
        digit /= ord(first) - 64
    elif first.islower():
        digit *= ord(first) - 96
    if last.isupper():
        digit -= ord(last) - 64
    elif last.islower():
        digit += ord(last) - 96
    return digit


def things(text):
    total = 0
    for word in text:
        word = word.strip()
        first_letter = word[0]
        last_letter = word[-1]
        digit = int(word[1:-1])
        total += summing(first_letter, digit, last_letter)
    return total


text = input().split()
print(f"{things(text):.2f}")
