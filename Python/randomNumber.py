import random

print(f"{random.random():.4f}") # Random float between 0.0 and 1.0
print(f"{random.random() * 10:.4f}") # Random float between 0.0 and 10.0

# Generate a random integer between x and y (both inclusive)
x = 1
y = 11
print(random.randint(x, y))

# Generate a random integer between x and y (y is exclusive here)
print(random.randrange(x, y))

#GENERATE EVEN NUMBER BETWEEN 1 AND 10
print(random.randrange(2, 11, 2))

#SELECT A SINGLE RANDOM ELEMENT FROM A SEQUENCE
dice = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
print(random.choice(dice))

#SELECT MULTIPLE RANDOM ELEMENTS FROM A SEQUENCE, DUPLICATES CAN BE THERE
print(random.choices(dice, k = 3))

#SELECT MULTIPLE RANDOM ELEMENTS FROM A SEQUENCE, NO DUPLICATES HERE
print(random.sample(dice, k = 3))

#SHUFFLE A SEQUENCE IN PLACE
cards = ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH"]
random.shuffle(cards)
print(cards)  

#EXERCISE 1 : GENERATING A RANDOM PASSWORD
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password_length = 12
for i in range(password_length):
    print(random.choice(characters), end="")
print()  

#EXERCISE 2 : GENERATING A RANDOM ONE-TIME PASSWORD(OTP)
otp_length = 6
for i in range(otp_length):
    print(random.randint(0, 9), end="")

otp = random.randrange(100000, 1000000)
print(f"\nYour One-Time Password (OTP) is: {otp}")

#RANDOM NUMBER GUESSING GAME
print("\nWelcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break