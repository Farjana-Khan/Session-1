# Assignment 25: Create a script that prints the current time and updates every second.

import datetime
import time

while True:
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(f"Current time: {now}", end='\r')  # \r returns the cursor to the beginning of the line
    time.sleep(1)  # Wait for 1 second
