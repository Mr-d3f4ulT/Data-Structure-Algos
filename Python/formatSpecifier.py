#format specifier = {value : flags} format a value based on the flags provided
#flags = <, >, ^, =, +, -, space, #, 0
# < = left align
# > = right align
# ^ = center align
# = = padding after the sign (if any) but before the digits
# + = show the sign for both positive and negative numbers
# - = show the sign only for negative numbers (default behavior)
# space = show a space before positive numbers and a minus sign before negative numbers
# # = show the base prefix for binary, octal, and hexadecimal numbers
# 0 = pad with zeros instead of spaces

number = 1234.56789

#rounding off the number to 2 decimal places, for n decimal places, use .nf where n is the number of decimal places you want to round off to
print(f"Rounded number to 2 decimal places: {number:.2f}")

#padding the number with zeros to make it 10 characters long, for n characters, use 0n where n is the number of characters you want to pad to
print(f"Number padded with zeros to 10 characters: {number:010.2f}")

#allocate n spaces for the number, for n spaces, use n where n is the number of spaces you want to allocate
print(f"Number allocated 15 spaces: {number:15.2f}")

