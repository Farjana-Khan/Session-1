#Assignment 10: Create a string that contains a simple bio data like name, age, and country. 
# Extract each piece of information and print them separately.

# Create a string that contains a simple bio data
bio_data = "Name: Borno, Age: 23, Country: Bangladesh"

# Extract and print each piece of information
name = bio_data[bio_data.find("Name:") + 6:bio_data.find(", Age:")]
age = bio_data[bio_data.find("Age:") + 5:bio_data.find(", Country:")]
country = bio_data[bio_data.find("Country:") + 9:]

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")
