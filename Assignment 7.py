# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades

# Create a list of tuples (student name, grade)
students = [("Araf", 85), ("Munqad", 92), ("Nazifa", 78), ("Arad", 88)]

# Sort the list by grades
students_sorted_by_grades = sorted(students, key=lambda x: x[1], reverse=True) #descending (True), ascending (False).

# Print the sorted list
print("Students sorted by grades:")
for student in students_sorted_by_grades:
    print(student)
