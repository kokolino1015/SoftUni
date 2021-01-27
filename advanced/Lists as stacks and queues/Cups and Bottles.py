from collections import deque

cups = deque(input().split(" "))
bottles = deque(input().split(" "))
wasted_water = 0

while cups:
    if bottles:
        current_cup = int(cups.popleft())
        current_bottle = int(bottles.pop())
        if current_cup <= current_bottle:
            wasted_water += current_bottle - current_cup
        elif current_bottle < current_cup:
            current_cup -= current_bottle
            cups.appendleft(current_cup)
    else:
        break
if not cups:
    bottles = [str(x) for x in bottles]
    print(f"Bottles: {' '.join(bottles)}\nWasted litters of water: {wasted_water}")
else:
    cups = [str(x) for x in cups]
    print(f"Cups: {' '.join(cups)}\nWasted litters of water: {wasted_water}")
