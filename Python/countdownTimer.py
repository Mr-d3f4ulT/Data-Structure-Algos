import time

# my_time = int(input("Enter the number of seconds to count down: "))
# for i in range(0, my_time):
#     print(f"{my_time - i} seconds remaining...")
#     time.sleep(1)

# print("HAPPY NEW YEAR!!!")

#A DIGITAL COUNTDOWN TIMER THAT TAKES THE NUMBER OF SECONDS AS INPUT AND COUNTS DOWN TO ZERO, PRINTING THE REMAINING TIME EVERY SECOND. ONCE THE COUNTDOWN REACHES ZERO, IT PRINTS A CELEBRATORY MESSAGE.

inputtime = int(input("Enter the time in seconds : "))

for x in range(inputtime, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    days = int(x / 86400)
    print(f"{days : 02d} days, {hours : 02d} hours, {minutes : 02d} minutes, {seconds : 02d} seconds remaining...")
    time.sleep(1)
