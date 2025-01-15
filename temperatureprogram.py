unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip().upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    # Celsius to Fahrenheit
    converted_temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {converted_temp} ℉")
    # Clothing suggestion based on Celsius
    if temp < 10:
        print("Time for the jacket.")
    elif temp > 25:
        print("Time for a T-shirt.")
    else:
        print("Time for a pullover.")
elif unit == "F":
    # Fahrenheit to Celsius
    converted_temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {converted_temp} ℃")
    # Clothing suggestion based on converted Celsius
    if converted_temp < 10:
        print("Time for the jacket.")
    elif converted_temp > 25:
        print("Time for a T-shirt.")
    else:
        print("Time for a pullover.")
else:
    print(f"{unit} is not a valid unit of measurement.")
