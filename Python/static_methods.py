# STATIC METHODS : A method that belongs to a class rather than any object from that class (instance)
#                  Usually used for general utility function

# Instance Method : Best for operations on instances of the class(objects)
# Static Methods : Best for utility functions that do not need access to class data

# Example of instance methods : def get_info(self):
#                                  return f"{self.name} = {self.position}"
# Example of static methods : def km_to_miles(kilometers):
#                                  return kilometers * 0.621371

class Employee:

  def __init__(self, name, position):
    self.name = name
    self.position = position
  
  def get_info(self):
    return f"{self. name} = {self.position}"
  
  @staticmethod
  def is_validPosition(position):
    valid_positions = [
      "Manager",
      "Janitor",
      "HR",
      "SDE"
    ]
    return position in valid_positions
  
print(Employee.is_validPosition("SDE")) # Only need class name to access static methods
print(Employee.is_validPosition("HOE"))

emp1 = Employee("Annie King", "HR")
emp2 = Employee("Johnny Sins", "SDE")

print(emp1.get_info())
print(emp2.get_info())