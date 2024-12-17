#Assignment 19: Write a script that processes a list of temperature readings.
# If any temperature is above a certain threshold, print a warning.

temperatures = [25, 30, 40, 35, 20, 45]
threshold = 35

for temp in temperatures:
    if temp > threshold:
        print(f"Warning: Temperature {temp}°C exceeds the threshold of {threshold}°C.")
    else:
        print(f"Temperature {temp}°C is within the safe range.")
