#Assignment 17: Write a script that simulates a basic login system. Check username and password correctness.

# Predefined credentials
correct_username = "user123"
correct_password = "pass456"

# User input
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
