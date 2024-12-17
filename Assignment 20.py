# Assignment 20: Create a script that processes a dictionary of products, 
# checking stock levels and generating restock alerts if necessary.

products = {
    "laptop": {"stock": 4, "min_required": 10},
    "smartphone": {"stock": 15, "min_required": 5},
    "tablet": {"stock": 2, "min_required": 8}
}

for product, details in products.items():
    stock = details["stock"]
    min_required = details["min_required"]
    if stock < min_required:
        print(f"Restock Alert: {product} has only {stock} in stock. Minimum required is {min_required}.")
    else:
        print(f"{product} stock is sufficient with {stock} units.")
