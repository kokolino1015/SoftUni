cards = input().split()
shuffle = int(input())
counter = len(cards) // 2

for i in range(shuffle):
    end = []
    for index in range(counter):
        first = cards[index]
        current_card = counter + index
        second = cards[current_card]
        end.append(first)
        end.append(second)
    cards = end

print(cards)