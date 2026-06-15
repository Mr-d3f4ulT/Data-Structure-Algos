#class Variables : Shared among all instances of a class
#                  Defined outside the constructors
#                  Allow you to share data among all objects created from that class

class Student:

  debut_year = 2021 #Can be accesed through any one of the objects, or name of the class can be used to access it(better practise)
  num = 0

  def __init__(self, name, age): #self refers to obj we currently working with
    self.name = name
    self.age = age
    Student.num += 1


stud1 = Student("Mille Morgan", 38)
stud2 = Student("Forest Faye", 23)

print(stud1.name)
print(stud1.debut_year)
print(stud2.name)
print(stud2.debut_year)
print(Student.debut_year)

print(Student.num)