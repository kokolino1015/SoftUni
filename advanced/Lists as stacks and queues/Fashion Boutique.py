stack = input().split(" ")
stack = [int(x) for x in stack]
capacity = int(input())

rack = 1
capacity_rack = 0

while stack:
    if capacity_rack + stack[-1] < capacity:
        capacity_rack += stack.pop()
    elif capacity_rack + stack[-1] == capacity:
        capacity_rack += stack.pop()
        if rack > 1:
            capacity_rack = 0
            rack += 1
    else:
        capacity_rack = 0
        rack += 1


print(rack)
