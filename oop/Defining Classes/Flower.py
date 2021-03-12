class Flower:
    def __init__(self, name, water_requirements):
        self.water_requirements = water_requirements
        self.name = name
        self.is_happy = False

    def water(self, water):
        if water >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        elif not self.is_happy:
            return f"{self.name} is not happy"
