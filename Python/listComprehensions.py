#List Comprehension = A concise way to create lists in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

double = []
for x in range (1, 11):
  double.append(x * 2)
print(double)

#-----------------------OR-----------------

doubles = [x * 2 for x in range(1, 11)]
print(doubles)

squares = [y ** 2 for y in range(1, 11)]
print(squares)

fruits = ["apple", "oranage", "banana", "coconut"]
fruit1 = [fruit.upper() for fruit in fruits]
print(fruits)
print(fruit1)

nums = [5, 4, 3, 2 , 1, 0, -1, -2 , -3, -4, -5, -6]
negativeNums = [num for num in nums if num < 0]
positiveNums = [num for num in nums if num >= 0]
positiveNums.sort()
print(positiveNums)
print(negativeNums)