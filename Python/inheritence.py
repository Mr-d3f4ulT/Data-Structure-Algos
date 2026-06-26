# Inheritence : Allows a class to inherit attributes and methods from another class
#               Helps with code resuability and extensibility
#            -> class Child(Parent)

class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animal):
  def speak(self):
    print("BHAW BHAW")

class Cat(Animal):
  pass

class Tiger(Animal):
  pass

dog = Dog("Shishimanu")
cat = Cat("Keyo")
tiger = Tiger("Sheraa")

print(dog.name)
dog.eat()
dog.speak()
print(cat.name)
print(tiger.name)
print("* "*40)

# MULTIPLE INHERITENCE : inherit from more than one parent class
#                        C(A, B)

class Prey:
  def flee(self):
    print("This animal is fleeing")

class Predator:
  def hunt(self):
    print("This animal is hunting")

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator):
  pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee() #as the fish inherit both parent class, it can access the methods of those parent class
fish.hunt()
print("* "*40)


# MULTI-LEVEL INHERITENCE : inherit at multiple levels
#                        A
#                        B(A)
#                        C(B)

class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating")
  def sleep(self):
    print(f"{self.name} is sleeping")

class Prey(Animal):
  def flee(self):
    print(f"{self.name} is fleeing")

class Predator(Animal):
  def hunt(self):
    print(f"{self.name} is hunting")

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator):
  pass

rabbit = Rabbit("Annie King")
hawk = Hawk("Daisy Phoenix")
fish = Fish("Juniper Ren")

rabbit.eat()
fish.eat()
fish.sleep()
fish.flee()
fish.hunt()