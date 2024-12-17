#Assignment 11: Create a formatted string that includes data from a list or dictionary. 
# For example, use a dictionary to store a person's information and format a string to include it.

# Create a dictionary with person's information
person_info = {
    "name": "Borno",
    "age": 30,
    "profession": "Student",
    "city": "Chittagong"
}

# Format a string to include the data
formatted_string = (
    f"My name is {person_info['name']}. "
    f"I am {person_info['age']} years old. "
    f"I work as a {person_info['profession']} and live in {person_info['city']}."
)
print(formatted_string)
