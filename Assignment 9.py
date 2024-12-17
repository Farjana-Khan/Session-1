# Assignment 9: Create a dictionary where keys are student names and values are lists of grades.
# Calculate the average grade for each student.

# Create a dictionary where keys are student names and values are lists of grades
students_grades = {
    'Alice': [85, 90, 88],
    'Bob': [78, 82, 91],
    'Charlie': [92, 87, 85],
    'Diana': [89, 76, 84]
}

# Calculate the average grade for each student
for name, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    print(f"Average grade for {name}: {average_grade:.2f}")
