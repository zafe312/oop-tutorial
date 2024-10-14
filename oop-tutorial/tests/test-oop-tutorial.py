import unittest
from oop_tutorial.base import Dog, Cat
from oop_tutorial.advanced import Car, Airplane, vehicle_sound

class TestOOPTutorial(unittest.TestCase):

    def test_animal_sounds(self):
        dog = Dog(name="Buddy", breed="Golden Retriever")
        self.assertEqual(dog.make_sound(), "Buddy says Woof!")

        cat = Cat(name="Whiskers", color="Gray")
        self.assertEqual(cat.make_sound(), "Whiskers says Meow!")

    def test_vehicle_movement(self):
        car = Car()
        airplane = Airplane()

        self.assertEqual(vehicle_sound(car), "Car is moving on roads.")
        self.assertEqual(vehicle_sound(airplane), "Airplane is flying in the sky.")

if __name__ == '__main__':
    unittest.main()
