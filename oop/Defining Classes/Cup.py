class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def can_fill(self, milliliters):
        return milliliters <= self.status()

    def fill(self, milliliters):
        if not self.can_fill(milliliters):
            return
        self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
