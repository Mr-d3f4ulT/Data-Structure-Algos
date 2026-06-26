# POLYMORPHISM : in nutshell, it means "Have many forms"
#             Two ways to achieve polymorphism :
#              1. Inheritence(Runtime Polymorphism/Method Overloading) : An object could be treated of the same type as a parent class
#              2. Duck Typing (Python-specific polymorphism)  : Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height


shapes = [
    Circle(4),
    Square(4),
    Triangle(3, 4)
]

for shape in shapes:
    print(shape.area())

#⭐⭐⭐⭐⭐⭐⭐⭐DUCK TYPING⭐⭐⭐⭐⭐⭐⭐⭐
#If it looks like duck, quacks like duck, it must be a duck
class Animal:
  alive = True

class Dog(Animal):
    def speak(self):
        print("WOOFF!!")

class Cat(Animal):
    def speak(self):
        print("MEOWW!!")

class Car:
    def speak(self):
        print("HONK!!") #Since our car object has enough methods to be considered as a duck, its a duck!!

animals = [
    Dog(),
    Cat(),
    Car()
]

for animal in animals:
    animal.speak()