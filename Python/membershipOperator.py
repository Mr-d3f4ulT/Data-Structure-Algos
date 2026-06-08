#Membership operator checks whether a value exist inside a sequence or collection
#Types : 1. in, 2. not in

nums = [10, 20, 30]

print(20 in nums) #Returns True
print(50 in nums) #Returns False
print(50 not in nums) #Returns True
print(20 not in nums) #Returns False
print()
#MEMBERSHIP in LOOPS
vowels = "aeiou"

for ch in "python":
    if ch in vowels:
        print(ch)
print()

#EXERCISE-1 : Email Validation
email = "koihnajane@gmail.com"

if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")