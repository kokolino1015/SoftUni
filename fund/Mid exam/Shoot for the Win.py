numbers = input().split(" ")
numbers = [int(x) for x in numbers]
shoot_count = 0

index = input()
while not index == "End":
    index = int(index)
    if index in range(len(numbers)):
        current_target = numbers[index]
        numbers[index] = -1
        shoot_count += 1
        for i in range(len(numbers)):
            if numbers[i] > current_target:
                numbers[i] -= current_target
            elif numbers[i] <= current_target:
                if numbers[i] == -1:
                    pass
                else:
                    numbers[i] += current_target
    index = input()

numbers = [str(x) for x in numbers]
print(f"Shot targets: {shoot_count} -> {' '.join(numbers)}")
