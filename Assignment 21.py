#Assignment 21: Write a function that calculates the factorial of a number and handles any potential errors.

def calculate_factorial(n):
    """Calculates the factorial of a number."""
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("The input must be a non-negative integer.")
        if n == 0 or n == 1:
            return 1
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial
    except ValueError as ve:
        print(f"Error: {ve}")

print(calculate_factorial(5))  
print(calculate_factorial(-5))  
print(calculate_factorial(3.5))  