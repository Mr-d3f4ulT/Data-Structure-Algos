#temperature Converter in Python

temperature = float(input("Enter the temperature in Celsius : "))
print("Choose the unit you want to convert the temperature to : ")
print("1. Fahrenheit")
print("2. Kelvin")

choice = int(input("Enter your choice (1-2) : "))
if choice == 1:
    converted_temperature = (temperature * 1.8) + 32
    unit = "Fahrenheit"
elif choice == 2:
    converted_temperature = temperature + 273.15
    unit = "Kelvin"
else:
    print("Invalid Choice! Please select a valid option (1-2).")
    exit()

print(f"The temperature in {unit} is : {converted_temperature:.2f} {unit}")