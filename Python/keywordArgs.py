#KEYWORD ARGUMENTS = An argument preceded by an identifier 
#                    helps with readibility 
#                    order of argument doesn't matter
#                    1. Positional, 2. Default, 3.Keyword, 4. Arbitrary

def hello(greeting, title, first, last):
  print(f"{greeting} {title} {first} {last}")

#hello("Hello", "Mr.", "Shivansh", "Pandey")
hello("Hello", first = "Shivansh", last = "Pandey",  title ="Mr.") #when we put the argument name before the value, then in whatever order we pass the arguments, it doesn't affect the desired output
