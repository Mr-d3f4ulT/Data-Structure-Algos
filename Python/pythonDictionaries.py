#DICTIONARIES : {} ordered, changeable, no duplicate keys, store in a {key:value} pair

capitals = {
  "USA" : "Washington D.C.", 
  "India" : "New Delhi", 
  "France" : "Paris", 
  "Japan" : "Tokyo", 
  "Germany" : "Berlin", 
  "Russia" : "Moscow", 
  "China" : "Beijing", 
  "Brazil" : "Brasilia", 
  "Australia" : "Canberra", 
  "Canada" : "Ottawa"
  }


#ACCESING VALUES
print(capitals.get("India")) #New Delhi
print(capitals["France"]) #Paris
print(capitals.get("Spain")) #None
print(capitals.get("Spain", "Not Found")) #Not Found, this is a default value if the key is not found, if not given it will return None as shown above
print()

#PRINT KEYS
print(capitals.keys())  
print(*capitals.keys()) #it will print the keys without the list format, * is used to unpack the list
for key in capitals.keys(): #it will print the keys without the list format, it is the same as above but using a loop
  print(key, end=", ") 
print()


#PRINT VALUES
print(capitals.values())
print(*capitals.values()) #it will print the values without the list format, * is
for value in capitals.values(): #it will print the values without the list format, it is the same as above but using a loop
  print(value, end=", ")
print()


#PRINT KEY-VALUE PAIRS
print(capitals.items())
print(*capitals.items()) #it will print the key-value pairs without the list format, * is used to unpack the list
for key, value in capitals.items(): #it will print the key-value pairs without the list format, it is the same as above but using a loop
  print(f"{key} -> {value}")
print()
student = {
    "name": "Shivansh",
    "age": 22,
    "course": "CSE"
}

#ADDING OR UPDATING KEY-VALUE PAIRS
student.update({"age": 23, "grade": "A"}) #it will update the age key and add a new key grade
print(student)
print()
#COPYING A DICTIONARY
student_copy = student.copy() #it will create a shallow copy of the student dictionary
print(student_copy)