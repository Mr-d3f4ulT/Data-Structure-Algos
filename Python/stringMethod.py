#STRING METHODS IN PYTHON

# input_string = input("Enter your name: ")
input_string = "   Shivansh Pandey!   "

print(f"Original String: {input_string}")

#finding length of the string
print(f"Length of the string: {len(input_string)}")

#converting to uppercase
print(f"Uppercase: {input_string.upper()}")

#converting to lowercase
print(f"Lowercase: {input_string.lower()}")

#removing leading and trailing whitespace 
print(f"Stripped String : {input_string.strip()}")

#replacing a substring
print(f"Replaced String : {input_string.replace('a', 'e')}")

#Finding in string
print(f"Index of 'a': {input_string.find('a')}") #returns the index of the first occurrence of 'a' in the string, or -1 if not found
print(f"Index of 'a': {input_string.rfind('a')}") #returns the index of the last occurrence of 'a' in the string, or -1 if not found

print(f"Capitalized String: {input_string.capitalize()}") #capitalizes the first character of the string and converts the rest to lowercase
print(f"Title Case String: {input_string.title()}") #capitalizes the first character of each word in the string and converts the rest to lowercase

print(f"Is the string alphanumeric? {input_string.isalnum()}") #returns True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, otherwise returns False
print(f"Is the string alphabetic? {input_string.isalpha()}") #returns True
print(f"Is the string numeric? {input_string.isdigit()}") #returns True if all characters in the string are digits and there is at least one character, otherwise returns False
print(f"Is the string whitespace? {input_string.isspace()}") #returns True if all characters in the string are whitespace and there is at least one character, otherwise returns False
print(f"Is string in uppercase? {input_string.isupper()}") #returns True if all caharacters in the string are uppercase and there is at least one character, otherwise returns False
print(f"Is string in lowercase? {input_string.islower()}") #returns True if all characters in the string are lowercase and there is at least one character, otherwise returns False