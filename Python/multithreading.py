# Multithreading : Used to perform multiple tasks concurrently(multitasking)
#                  Good for I/O bound tasks like reading file sor fetching data from APIs
#                  threading.Thread(target = my_function)
import threading
import time

def walk_dog():
  time.sleep(8)
  print("walking done")

def take_trash_out():
  time.sleep(2)
  print("Trash out")

def get_mail():
  time.sleep(4)
  print("New Mail")

# walk_dog()
# take_trash_out()
# get_mail()

task1 = threading.Thread(target = walk_dog)
task1.start()
task2 = threading.Thread(target = take_trash_out)
task2.start()
task3 = threading.Thread(target = get_mail)
task3.start()

task1.join()
task2.join()
task3.join()

print("ALL TASKS DONE")