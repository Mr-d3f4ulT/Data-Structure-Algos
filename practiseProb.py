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
print(B//A)  #Floor Division operator results in Integer