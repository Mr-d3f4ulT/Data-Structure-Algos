import time

my_time = int(input("Enter the number of seconds to count down: "))
for i in range(0, my_time):
    print(f"{my_time - i} seconds remaining...")
    time.sleep(1)

print("HAPPY NEW YEAR!!!")