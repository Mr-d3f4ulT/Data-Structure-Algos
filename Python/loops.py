# WHILE LOOP

#name = input("What is your name :- ")
# while name == "":
#     print("You didn't enter a name.")
#     name = input("What is your name :- ")
# else:
#     print(f"Wassup {name}!")

# food = input("What is your favourite food(type 'exit' to quit) :- ")

# while not food == 'exit':
#     print(f"You like {food}!")
#     food = input("Enter another favourite food(type 'exit' to quit) :- ")

# print("Goodbye!")    

num = int(input("Enter a number between 1 - 10 :-"))

while num < 1 or num > 10:
    print("Invalid number, try again.")
    num = int(input("Enter a number between 1 - 10 :-"))

# FOR LOOP

for i in range(5): #loop starts at 0 and ends at 4
    if i == 2:
        continue
    print(f"i is currently {i}")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break 

for x in "banana":
  print(x)
  if x == 'a':
    print("@")

for i in range(1, 11):  #loop starts at 1 and ends at 10
    print(i)

for i in range(1, 11, 2):  #loop starts at 1, ends at 10 and increments by 2
    print(i)
