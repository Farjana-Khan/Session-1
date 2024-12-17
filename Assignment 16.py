#Assignment 16: Create a script that checks if 
# a person is eligible for a senior citizen discount based on age and residency.

age = int(input("Enter your age: "))
is_resident = input("Are you a local resident? (yes/no): ").lower() == "yes"

if age >= 60 and is_resident:
    print("You are eligible for the senior citizen discount.")
else:
    print("You are not eligible for the discount.")
