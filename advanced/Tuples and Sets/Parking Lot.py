def solve(n):
    cars = set()
    for i in range(n):
        command = input().split(", ")
        if command[0] == "IN":
            cars.add(command[1])
        elif command[0] == "OUT":
            cars.remove(command[1])
    if cars:
        for i in cars:
            print(i)
    else:
        print("Parking Lot is Empty")


solve(int(input()))
