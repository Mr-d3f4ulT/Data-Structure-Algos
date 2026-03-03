#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start:stop:step]
#in positive slicing, the start index is inclusive and the stop index is exclusive
#in negative slicing, the start index is exclusive and the stop index is inclusive

credit_card_number = "1234 5678 9012 3456"

#accessing the first 4 digits of the credit card number
print(f"First four digits are : {credit_card_number[:4]}")
#accessing the middle 4 digits of the credit card number
print(f"Middle four digits are : {credit_card_number[5:9]}")
#accessing the last 4 digits of the credit card number
print(f"Last four digits are : {credit_card_number[-4:]}") #-4 is negative slicing which means it starts from the end of the string and goes backwards

