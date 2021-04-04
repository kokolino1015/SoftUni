class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal):
        if Vet.space > 0:
            Vet.space -= 1
            self.animals.append(animal)
            Vet.animals.append(animal)
            return f"{animal} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal):
        if animal in self.animals:
            Vet.space += 1
            self.animals.remove(animal)
            Vet.animals.remove(animal)
            return f"{animal} unregistered successfully"
        return f"{animal} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
