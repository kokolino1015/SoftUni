numbers = input().split(" ")
average = int(input())
numbers = list(map(lambda x: int(x) * average, numbers))
filtered = list(filter(lambda x: x >= (sum(numbers) / len(numbers)), numbers))
if len(filtered) >= len(numbers) / 2:
    print(f"Score: {len(filtered)}/{len(numbers)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(numbers)}. Employees are not happy!")
