from collections import deque

run = int(input())

stack = deque()
for i in range(run):
    query = input().split(' ')
    query_type = query[0]
    if query_type == "1":
        query_element = query[1]
        stack.appendleft(int(query_element))

    elif query_type == "2":
        if len(stack) == 0:
            pass
        else:
            stack.popleft()

    elif query_type == "3":
        if len(stack) == 0:
            pass
        else:
            print(max(stack))

    elif query_type == "4":
        if len(stack) == 0:
            pass
        else:
            print(min(stack))

stack = list(map(lambda x: str(x), stack))
print(", ".join(stack))
