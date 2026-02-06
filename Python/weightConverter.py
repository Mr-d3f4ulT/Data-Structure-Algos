#PYTHON WEIGHT CONVERTER PROGRAM

weight = float(input("Enter your current weight in kilograms : "))

print("Choose the unit you want to convert your weight to : ")
print("1. Grams")
print("2. Pounds")
print("3. Ounces")

choice = int(input("Enter your choice (1-3) : "))

if choice == 1:
    converted_weight = weight * 1000
    unit = "Grams"
elif choice == 2:
    converted_weight = weight * 2.20462 
    unit = "Pounds(lbs)"
elif choice == 3:
    converted_weight = weight * 35.274
    unit = "Ounces(oz)"
else:
    print("Invalid choice! Please select a valid option (1-3).")
    exit()

print(f"Your weight in {unit} is: {converted_weight:.2f} {unit}")