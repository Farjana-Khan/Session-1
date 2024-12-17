# Assignments: Write a regex to find the Bangladesh phone number with all variations.
# 01454565767
# +880196345634
# 0088785674657
# 01845-567567

import re

def validate_bangladesh_phone_number(phone_number):
    pattern = r'^(?:(?:\+88|0088|88)?01[3-9]\d{8})$'
    return bool(re.match(pattern, phone_number))

# Test cases
test_numbers = [
    "+8801812345678",
    "008801812345678",
    "01812345678",
    "01712345678",
    "01612345678",
    "01912345678",
    "01412345678",
    "+88 01812345678",  # Invalid due to space
    "0181234567",       # Invalid: only 10 digits
]

for number in test_numbers:
    print(f"{number}: {'Valid' if validate_bangladesh_phone_number(number) else 'Invalid'}")
