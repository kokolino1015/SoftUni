from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_conditioners = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        if distance * (self.fuel_consumption + self.air_conditioners) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.air_conditioners)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_conditioners = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        if distance * (self.fuel_consumption + self.air_conditioners) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.air_conditioners)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
