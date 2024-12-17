# Assignment 8: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.

# Create a dictionary representing a student
student = {
    'name': 'Borno',
    'roll_number': 12345,
    'grades': {'Math': 88, 'Science': 92, 'English': 85}
}

# Perform various operations

# Adding a new subject and grade
student['grades']['History'] = 79
print("After adding a new subject:", student)

# Modifying an existing grade
student['grades']['Math'] = 95
print("After modifying Math grade:", student)

# Removing a subject
removed_grade = student['grades'].pop('History')
print("Removed grade:", removed_grade)
print("After removing History:", student)

# Updating personal information
student.update({'email': 'borno.25@example.com', 'age': 21})
print("After updating personal information:", student)
