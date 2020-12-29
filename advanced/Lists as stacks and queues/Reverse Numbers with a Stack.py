text = input().split(" ")
stack = [int(x) for x in text if x != ""]

while stack:
    print(stack.pop(), end=" ")
