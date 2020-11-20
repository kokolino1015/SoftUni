class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        res = ""
        if species == "mammal":
            res += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            res += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            res += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        res += f"Total animals: {Zoo.__animals}"
        return res


zoo_name = input()
zoo = Zoo(zoo_name)
lines = int(input())

for i in range(0, lines):
    animals = input().split(" ")
    species = animals[0]
    name = animals[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))