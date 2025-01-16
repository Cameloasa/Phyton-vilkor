print("Hi, shall we check the temperature?")

# Prompt the user for the unit and validate input
while True:
    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip().upper()
    if unit in ["C", "F"]:
        break
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit. Try again.")

try:
    temp = float(input("Enter the temperature: "))

    if unit == "C":
        # Celsius to Fahrenheit
        converted_temp = round((9 * temp) / 5 + 32, 1)
        print(f"The temperature in Fahrenheit is: {converted_temp} ℉")
        # Clothing suggestion using `and`
        if temp < 10:
            print("Take your jacket because it's cold outside.")
        elif 10 <= temp <= 25:
            print("It's neither cold nor warm outside, so maybe you need a pullover.")
        else:
            print("It's warm outside, so you need just a T-shirt.")
    elif unit == "F":
        # Fahrenheit to Celsius
        converted_temp = round((temp - 32) * 5 / 9, 1)
        print(f"The temperature in Celsius is: {converted_temp} ℃")
        # Clothing suggestion using `and`
        if converted_temp < 10:
            print("Take your jacket because it's cold outside.")
        elif 10 <= converted_temp <= 25:
            print("It's neither cold nor warm outside, so maybe you need a pullover.")
        else:
            print("It's warm outside, so you need just a T-shirt.")
except ValueError:
    print("Invalid input. Please enter a numeric temperature.")

print("Have a nice day!")


"""
Celsius: -5°C -> Take your jacket because it's cold outside.
Celsius: 15°C -> It's neither cold nor warm outside, so maybe you need a pullover.
Celsius: 30°C -> It's warm outside, so you need just a T-shirt.
Fahrenheit: 20°F -> Take your jacket because it's cold outside.
Fahrenheit: 68°F -> It's neither cold nor warm outside, so maybe you need a pullover.
Fahrenheit: 90°F -> It's warm outside, so you need just a T-shirt.
"""
