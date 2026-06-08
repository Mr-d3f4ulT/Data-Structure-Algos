#TUPLES : () ordered, unchangeable, allows duplicate values, FASTER

myTuple = ("apple", "banana", "cherry")
print(myTuple)
print(myTuple[1]) #banana

#LENGTH of TUPLE
print(len(myTuple)) 


#CHECK if ITEM exists in TUPLE
if "apple" in myTuple:
    print("Yes, 'apple' is in the tuple")


#CHANGE TUPLE to LIST to MODIFY
myList = list(myTuple)
myList[1] = "kiwi"
myTuple = tuple(myList)
print(myTuple) #('apple', 'kiwi', 'cherry')

#COUNTING ITEMS in TUPLE
print(myTuple.count("apple")) #1

#GETTING INDEX of ITEM in TUPLE
print(myTuple.index("kiwi")) #1

#ADDING ITEMS to TUPLE (creates a new tuple)
myTuple += ("orange",)
print(myTuple) #('apple', 'kiwi', 'cherry', 'orange')