#Assignment 12: Write a function that takes a string and returns a dictionary 
# with the counts of each character in the string.

# Function to count characters in a string
def count_characters(input_string):
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

# Test the function
sample_string = "Hello, Python learners!"
char_count_result = count_characters(sample_string)
print("Character counts:", char_count_result)
