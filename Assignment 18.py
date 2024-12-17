#Assignment 18: Implement a system that categorizes a day based on temperature and weather conditions.

temperature = int(input("Enter the temperature in Celsius: "))
weather = input("Enter the weather (sunny/rainy/snowy): ").lower()

if weather == "sunny":
    if temperature > 25:
        print("It's a beach day!")
    else:
        print("Enjoy the sunshine, but it's not warm enough for the beach.")
elif weather == "snowy":
    if temperature < 0:
        print("It's a perfect day for skiing!")
    else:
        print("It's snowy, but not cold enough for skiing.")
elif weather == "rainy":
    print("It's a stay-home day. Relax and enjoy!")
else:
    print("Weather condition not recognized. Stay prepared for anything!")
