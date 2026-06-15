#OBJECT ORIENTED PROGRAMMING

#object = a "bundle" of related attributes(variables) and methods(functions) 
#         Ex: phone, book, cup
#         You need a "class" to create many objects
#class = (blueprint) used to design the structure and layout of an object


class Car:
  def __init__(self, model, year, color): #dunder or double underscore (__init__(self)) is the constructor
    self.model = model
    self.year = year
    self.color = color

  def drive(self):
    print(f"You're driving a {self.year} {self.model}")

car1 = Car("BMW M5 Competition", 2024, "Matt Black")
print(car1.model)
print(car1.year)
print(car1.color)
car1.drive()
print()
car2 = Car("Porsche 991 GT3 RS", 2025, "Dark Grey")
print(car2.model)
print(car2.year)
print(car2.color)
car2.drive()
