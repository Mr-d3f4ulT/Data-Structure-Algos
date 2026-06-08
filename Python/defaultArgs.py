
#DEFAULT ARGUMENTS = A default value for a certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces number of arguments
#                    1. Positional, 2. Default, 3. Keyword, 4. Arbitary

def net_price(list_price, discount, tax):
  return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.04)) 

#This will work, but let's say we pass only 500 as argument, and have default value for discount and tax preset, until we pass them as argument too

def net_price1(list_price, discount= 0, tax = 0.03):
  return list_price * (1 - discount) * (1 + tax)
print(net_price1(530))
print(net_price1(530, 0.1))
print(net_price1(530, 0.1, 0))

#COUNTDOWN TIMER
import time

def count(end, start = 1): #DEFAULT ARGUMENT MUST BE AFTER NON-DEFAULT ARGUMENT
  for x in range(start, end + 1):
    print(x, end = ' -> ')
    time.sleep(1)
  print("TIME UP!!")

count(5)