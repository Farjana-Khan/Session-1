#Assignment 5: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.

# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print("Element at (1, 1):", matrix[1][1])  

# Modify an element
matrix[2][2] = 99
print("Modified Matrix:")
for row in matrix:
    print(row)

# Iterate through the matrix
print("Iterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
