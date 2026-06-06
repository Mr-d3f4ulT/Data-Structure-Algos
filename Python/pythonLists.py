#COLLECTIONS : single "variables" used to store multiple values
      #LISTS : [] ordered, changeable, allows duplicate values
      #SETS : {} unordered, immutable, no duplicate values
      #TUPLES : () ordered, unchangeable, allows duplicate values
      #DICTIONARIES : {} unordered, changeable, no duplicate keys

my_list = [1, 2, 2, 3, 4, 5, 5]


# #FINDING SQUARE OF EVEN NUMBERS IN A LIST
# #method 1 : using for loop and if statement
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = []
# for i in numbers:
#     if i % 2 == 0:
#         squares.append(i ** 2)
# print(squares)

# #method 2 : using list comprehension
# squares2 = [i ** 2 for i in numbers if i % 2 == 0]
# print(squares2)

#Printing the elements of list
print(my_list[0:])
print(my_list[0:7])
print(my_list[::-1])
print()

list1 = [5, 2, 9, 1, 5, 6]
#SORTING LIST

#method 1 : using sort() method
print(f"Original list: {list1}")
list1.sort()
print(f"Sorted list: {list1}")
print()

#FINDING LENGTH OF A LIST
length = len(list1)
print(f"Length of the list: {length}")
print()

#ADDING ELEMENTS IN LIST
list1.append(10)
print(f"List after adding element 10: {list1}")
print()

#COPYING A LIST
list2 = list1.copy()
print(f"Copied list: {list2}")
print()

#REMOVING ELEMENTS FROM A LIST
list1.remove(5)  #removes first occurrence of 5
print(f"List after removing element 5: {list1}")
print()

#COUNTING OCCURRENCES OF AN ELEMENT IN A LIST
count = list1.count(5)
print(f"Number of occurrences of 5 in the list: {count}")
print()

#INSERTING ELEMENTS IN A LIST
list1.insert(2, 15)  #inserts 15 at index 2
print(f"List after inserting element 15 at index 2: {list1}")
print()

#RETURINING THE INDEX OF AN ELEMENT IN A LIST   
index = list1.index(9)
print(f"Index of element 9 in the list: {index}")
print()

#REVERSING A LIST
list1.reverse()
print(f"Reversed list: {list1}")
print()

#CLEARING A LIST
list1.clear()
print(f"List after clearing: {list1}")
print()