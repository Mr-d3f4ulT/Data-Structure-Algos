#Iterables = An object/collection that can  return its elements one at a time, allowing it to be iterated over in a loops
#ex : list, tuple, string, dictionary, set, range

#ITERABLE is a collection that can produce an iterator
#ITERATOR is an object that remembers its current position and gives the next element when requested, use iter() to create an iterator

#LIST
nums = [1, 2, 3]

for n in nums:
    print(n)
print()

#STRING
name = "AnnaClairClouds"
for ch in name:
  print(ch, end = ", ")
print()

#TUPLE
data = (10, 20, 30)

for item in data:
    print(item)
print()

#SET
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
print()

#DICTIONARY
student = {
    "name": "Shivansh",
    "age": 24
}

for key in student:
    print(key)
print()
for value in student.values():
    print(value)
print()
for key,value in student.items():
    print(f"{key} : {value}")
print()

#RANGE
for i in range(5):
    print(i)