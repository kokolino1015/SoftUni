class Town:
    def __init__(self):
        self.towns = {}
        self.getting_town()

    def getting_town(self):
        command = input()
        while not command == "Sail":
            token = command.split("||")
            town = token[0]
            population = int(token[1])
            gold = int(token[2])
            if town not in self.towns:
                self.towns[town] = [town, population, gold]
            elif town in self.towns:
                value = self.towns[town]
                population += int(value[1])
                gold += int(value[2])
                self.towns[town] = [town, population, gold]
            command = input()
        self.solve()

    def solve(self):
        command = input()
        while not command == "End":
            token = command.split('=>')
            action = token[0]
            town = token[1]
            if action == "Plunder":
                self.plunder(town, int(token[2]), int(token[3]))
            elif action == 'Prosper':
                self.prosper(town, int(token[2]))
        self.print()

    def plunder(self, town, population, gold):
        value = self.towns[town]
        town_population = value[1]
        town_gold = value[2]
        town_population -= int(population)
        town_gold -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {population} citizens killed.")
        if town_gold > 0 and town_population > 0:
            self.towns[town] = [town, town_population, town_gold]
        else:
            self.towns.pop(town)
            print(f"{town} has been wiped off the map!")
        self.solve()

    def prosper(self, town, gold):
        value = self.towns[town]
        town_gold = value[2]
        if int(gold) > 0:
            town_gold += int(gold)
            self.towns[town] = [town, value[1], town_gold]
            print(f"{gold} gold added to the city treasury. {town} now has {town_gold} gold.")
        else:
            print("Gold added cannot be a negative number!")
        self.solve()

    def print(self):
        print(f"Ahoy, Captain! There are {len(self.towns)} wealthy settlements to go to:")
        dictionary = sorted(self.towns.values(), key=lambda x: (-(x[2]), x[0]))
        for key in dictionary:
            town = key[0]
            people = key[1]
            gold = key[2]
            print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
        exit()


res = Town()
