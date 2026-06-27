# CLASS METHOD : Allow operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself

class Student:

  count = 0

  def __init__(self, name, gpa):
    self.name = name
    self.gpa = gpa
    Student.count += 1

  def getinfo(self):
    return f"{self.name} = {self.gpa}"
  
  @classmethod
  def getCount(cls):
    return f"Total : {cls.count}"
  

s1 = Student("ABC", 2.9)
s2 = Student("BCD", 3.5)
s3 = Student("XYZ", 4.0)

print(s1.getinfo())
print(s2.getinfo())
print(s3.getinfo())
print(Student.getCount())