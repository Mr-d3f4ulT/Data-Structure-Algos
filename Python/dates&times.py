from datetime import *
now = datetime.now()

#print current date & time
print(datetime.now())

#Print current date only
print(date.today())

#print current time only
print(now.time())

#indivisual components

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#Creating own date
birthday = datetime(2002, 7, 13, 8, 59, 32)

print(birthday)

#formating date
print(now.strftime("%d.%m.%Y")) # print date like 29.06.2026
print(now.strftime("%d.%m.%y")) # print date like 29.06.26
# Common Format Codes
#  | Code	|    Meaning	      |
#  |  %d  |    Day	          |
#  |  %m  |    Month	        |
#  |  %Y  |    4-digit Year	  |
#  |  %y  |    2-digit Year	  |
#  |  %H  |    Hour (24-hour)	|
#  |  %I  |    Hour (12-hour)	|
#  |  %M  |    Minute	        |
#  |  %S  |    Second	        |
#  |  %A  |    Full weekday	  |
#  |  %a  |    Short weekday	|
#  |  %B  |    Full month	    |
#  |  %b  |    Short month	  |
#  |  %p  |    AM/PM	        |

#date difference
d1 = datetime(2026, 6, 1)
d2 = datetime(2026, 1, 7)

print(d1 - d2)

#compare dates
print(d1 > d2)

#timestamp
print(now.timestamp()) #seconds since January 1, 1970

#ISO Format
print(now.isoformat())