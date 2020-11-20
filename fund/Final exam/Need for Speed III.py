class Car:
    def __init__(self):
        self.times = int(input())
        self.cars = {}
        self.getting_cars()

    def getting_cars(self):
        for i in range(self.times):
            car = input().split("|")
            mark = car[0]
            mileage = int(car[1])
            fuel = int(car[2])
            self.cars[mark] = [mark, mileage, fuel]
        self.solve()

    def solve(self):
        command = input()
        while not command == "Stop":
            token = command.split(" : ")
            if token[0] == "Drive":
                self.drive(token[1], int(token[2]), int(token[3]))
            elif token[0] == "Refuel":
                self.refuel(token[1], int(token[2]))
            elif token[0] == "Revert":
                self.revert(token[1], int(token[2]))
            command = input()
        self.print()

    def drive(self, car, distance, fuel):
        value = self.cars[car]
        if int(value[2]) - fuel >= 0:
            self.cars[car] = [car, value[1] + distance, value[2] - fuel]
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if int(value[1]) + distance >= 100000:
                print(f"Time to sell the {car}!")
                self.cars.pop(car)
        else:
            print("Not enough fuel to make that ride")
        self.solve()

    def refuel(self, car, fuel):
        value = self.cars[car]
        gas = int(value[2])
        getet = 0
        if gas + fuel > 75:
            getet += 75 - gas
        else:
            getet += fuel
        self.cars[car] = [car, value[1], gas + getet]
        print(f"{car} refueled with {getet} liters")
        self.solve()

    def revert(self, car, kilometers):
        value = self.cars[car]
        km = int(value[1])
        getet = 0
        if km - kilometers < 10000:
            self.cars[car] = [car, 10000, value[2]]
        elif km - kilometers > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
            self.cars[car] = [car, km - kilometers, value[2]]
        self.solve()

    def print(self):
        dictionary = sorted(self.cars.values(), key=lambda x: (-int(x[1]), x[0]))
        for i in dictionary:
            print(f"{i[0]} -> Mileage: {i[1]} kms, Fuel in the tank: {i[2]} lt.")
        exit()


res = Car()
