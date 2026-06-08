# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator

def display_name(*args):
  for arg in args:
    print(arg, end = ' ')

display_name("Er.", "Shivansh", "Pandey", "II") #WE CAN ADD AS MANY NUMBER OF NON KEY ARGS, cause they all we be treated as one single tuple


def print_address(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")

print_address(street="123 Anal St.", city="Detriot", state="MI", zipcode="53251")
print()

#USING BOTH *args and **kwargs
def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()
  for value in kwargs.values():
    print(value, end = " ")


shipping_label("Er.", "Shivansh", "Pandey", "II", 
                street="123 Anal St.", 
                city="Detriot", 
                state="MI", 
                zipcode="53251")