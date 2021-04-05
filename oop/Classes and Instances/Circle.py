class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        area = Circle.pi * self.radius ** 2
        return round(area, 2)

    def get_circumference(self):
        circumference = 2 * Circle.pi * self.radius
        return round(circumference, 2)
