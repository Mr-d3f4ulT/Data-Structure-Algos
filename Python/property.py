# @property : Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit : Add additional logic when read, write, or delete attributes
#             Gives u getter, setter, and deleter method
#             Lets you control how an attribute is accessed, modified, or deleted, while making it look like a normal variable.

# class Student:
#   def __init__(self, name):
#     self._name = name
# #Now if i want to print this in upper case without using @property
#   # def get_name(self):
#   #   return self.name.upper()
# #With @property
#   @property #<---- GETTER
#   def name(self):
#     return self._name.upper()
  
# s1 = Student("Shivansh Pandey")
# print(s1.name)
# # print(s1.get_name())

class Student:

    def __init__(self, age):
        self._age = age

    # Getter
    @property
    def age(self):
        return self._age

    # Setter
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # Deleter
    @age.deleter
    def age(self):
        print("Age deleted")
        del self._age

s1 = Student(23)
print(s1.age)
s1.age = 24
print(s1.age)
del s1.age
