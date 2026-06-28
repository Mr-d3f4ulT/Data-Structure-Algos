# EXCEPTION : An event that interupts the flow of program
#             (ZeroDivisonError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

# num = int(input("Enter a number: "))

# try:
#     result = 100 / num
#     print(result)
# except:
#     print("You have entered 0, pls re-enter a valid number")

#Handling specific exception
# try:
#     num = int("abc")
# except ValueError:
#     print("Can't convert string into a number")

# #Handling multiple exceptions
# try:
#     a = int(input())
#     print(10 / a)

# except ValueError:
#     print("It's not a number, pls enter a number")

# except ZeroDivisionError:
#     print("You've entered zero, it's invalid")

#Exception as e : to check which type of error is comming
# try:
#     print(10/0)
# except Exception as e:
#     print(e)

#Using finally : it will always execute wheather an error comes or not
# try:
#     print(10/0)
# except:
#     print("Error!!")
# finally:
#     print("Program Finished")

#Else : this will execute only if no exception comes in try-except block
try:
    print(10 / 2)

except:
    print("Error")

else:
    print("Everything is fine")

#Raise : If user wants to create an exception
age = int(input("enter age : "))
if age < 18:
    raise Exception("Age must be above 18yrs")