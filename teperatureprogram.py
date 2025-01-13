unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    # Celsius to Fahrenheit
    converted_temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {converted_temp} ℉")
elif unit == "F":
    # Fahrenheit to Celsius
    converted_temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {converted_temp} ℃")
else:
    print(f"{unit} is not a valid unit of measurement.")