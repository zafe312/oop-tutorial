# advanced.py
from abc import ABC, abstractmethod

# Abstract Base Class Example
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# Demonstrating polymorphism
class Car(Vehicle):
    def move(self):
        return "Car is moving on roads."

class Airplane(Vehicle):
    def move(self):
        return "Airplane is flying in the sky."

def vehicle_sound(vehicle):
    return vehicle.move()