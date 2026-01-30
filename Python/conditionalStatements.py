print("We will learn conditional statements in python")

#Program to check if a number is positive, negative or zero
# num = float(input("Enter a number : "))
# if num > 0:
#     print("The number is positive")
# elif num == 0:
#     print("The number is zero")
# else:
#     print("The number is negative")

#Program to check if a number is prime or not
# n = int(input("Enter a number : "))
# if n < 2:
#     print(f"{n} is not a prime number")
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print(f"{n} is not a prime number")
#             break
#     else:
#         print(f"{n} is a prime number")

#Program to find the largest of three numbers
a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c
    print(f"The largest number among {a}, {b} and {c} is {largest}")