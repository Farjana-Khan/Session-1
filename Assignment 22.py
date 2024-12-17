#Assignment 22: Write a script that reads a CSV file containing product information and converts it into a JSON file.



import csv
import json

# Reading data from CSV file
products = []
with open('/Users/mac/Documents/Python_Field Work/products.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # Read CSV as dictionaries
    for row in csv_reader:
        products.append(row)

# Writing data to JSON file
with open('data products.json', 'w') as json_file:
    json.dump(products, json_file, indent=4)

print("CSV data successfully converted to JSON.")