#super() : used within a child class to call methods from a parent class (superclass)
#          Allows you to extend the functionality of the inherited methods

class Shape:
  def __init__(self, color, filled):
    self.color = color
    self.filled = filled
class Circle(Shape):
  def __init__(self, color, filled, radius):
    super().__init__(color, filled)
    self.radius = radius

class Square(Shape):
  def __init__(self, color, filled, sides):
    super().__init__(color, filled)
    self.sides = sides

class Triangle(Shape):
  def __init__(self, color, filled, width, height):
    super().__init__(color, filled)
    self.width = width
    self.height = height

circle = Circle(color="Red", filled=True, radius=5)
square = Square(color="Yellow", filled=True, sides=5)
triangle = Triangle(color="Blue", filled=True, width=4, height=4)

print(circle.color)
print(circle.radius)