#COLLECTIONS : single "variables" used to store multiple values
      #LISTS : [] ordered, changeable, allows duplicate values
      #TUPLES : () ordered, unchangeable, allows duplicate values
      #SETS : {} unordered, unchangeable, no duplicate values
      #DICTIONARIES : {} unordered, changeable, no duplicate keys

my_list = [1, 2, 2, 3, 4, 5, 5]
my_tuple = (1, 2, 2, 3, 4, 5, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


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
