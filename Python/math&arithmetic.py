x = 3.14
y= -4
z = 5

print(round(x, 1)) #round to 1 decimal place 
print(f"The absolute value of y is {abs(y)}") #absolute value of y

#print sum
a = 10
b = 20
print(f"Value of a is {a}")
print(f"Value of b is {b}")
print(f"the sum of a and b is {a + b}")

#Expression execution
A,B = 5, 10
print(f"Value of A is {A}")
print(f"Value of B is {B}")
print()
Txt = "*"
print(2 * A * Txt + " " + 3 * B * Txt)  #String and Numeric Values can operate together in expression using *

a,b = '2', 3
print((a + Txt + " ")*b)  #String and String can operate together in expression using +

C = 4
print(A + B * C)  #Numeric Values can operate with all arithimetic operators
print((A + B) * C)  #Parenthesis has highest precedence in expression evaluation

D = 50.2

print(C * D)  #Arithmetic operation between Integer and Float results in Float
print(int(D))  #Type casting Float to Integer

print(B/A)  #Division operator results in Float
print(B//A)  #Floor Division operator results in Integer ex - 7.99 becomes 7
print(B%A)  #Modulus operator results in Remainder Value, remainder is negative if denominator is negative
print(B**A)  #Exponentiation operator results in Power Value
print(pow(B,A))  #pow() function also results in Power Value


print(f"The maximum value among A, B and C is {max(A,B,C, D)}")  #max() function returns the maximum value among the arguments
print(f"The minimum value among A, B and C is {min(A,B,C, D)}")  #min() function returns the minimum value among the arguments