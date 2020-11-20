def check(word, valid):
    left_check = word[:10]
    right_check = word[10:]
    for index in valid:
        num = 9
        for number in range(4):
            if (index in left_check and left_check.count(index) == 10) \
                    and (index in right_check and right_check.count(index) == 10):
                return print(f'ticket "{word}" - 10{index} Jackpot!')
            elif (index * num) in left_check and (index * num) in right_check:
                return print(f'ticket "{word}" - {min(left_check.count(index), right_check.count(index))}{index}')
            num -= 1
    return print(f'ticket "{word}" - no match')


ticket = input().replace(" ", " ").split(",")
valid = "@", "#", "$", "^"
for word in ticket:
    word = word.strip()
    if len(word) != 20:
        print("invalid ticket")
        continue
    check(word, valid)
