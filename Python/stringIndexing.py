#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start:stop:step]

credit_card_number = "1234 5678 9012 3456"

#accessing the first 4 digits of the credit card number
print(f"First four digits are : {credit_card_number[:4]}")
#accessing the middle 4 digits of the credit card number
print(f"Middle four digits are : {credit_card_number[5:9]}")
#accessing the last 4 digits of the credit card number
print(f"Last four digits are : {credit_card_number[-4:]}")

