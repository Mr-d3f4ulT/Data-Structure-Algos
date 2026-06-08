#SETS : {} unordered, immutable, no duplicate values
#empty_set = set()     # This is how you create an empty set!
juice = {2, 2, 1, 3, 3, 4, 5, 6 ,7, 8, 9, 10}

print(juice)  #duplicates will be removed and order is not guaranteed


#Adding values to a set
juice.add(11)
print(f"Added element 11 to the set: {juice}")
print()

#Removing values from a set
juice.remove(2)
print(f"Removed element 2 from the set: {juice}")
print()

#Checking if an element is in the set
print(f"Is 3 in the set? {'Yes' if 3 in juice else 'No'}")
print()

#Set operations
other_set = {5, 6, 7, 8, 9, 10, 11, 12}
print(f"Union of juice and other_set: {juice.union(other_set)}")
print()

print(f"Intersection of juice and other_set: {juice.intersection(other_set)}")
print()

print(f"Difference of juice and other_set: {juice.difference(other_set)}")
print()

print(f"Symmetric difference of juice and other_set: {juice.symmetric_difference(other_set)}")
print()

#Iterating through a set

print("Iterating through the set:")
for item in juice:
    print(item, end=' ')

print()

#print(juice[1])  # This will raise an error because sets do not support indexing

#Copying a set
juice_copy = juice.copy()
print(f"Copied set: {juice_copy}")
print()

#CLEARING a set
juice_copy.clear()
print(f"Cleared copied set: {juice_copy}")