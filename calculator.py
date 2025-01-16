# create a calculator witch handles + - * /  and outputs answer based on the mode operator used
# use 3 separate inputs
# extend functionality with extra code so it's also transforme Celsius to Fahrenheit
print("if-elif-else statements")

print("Welcome to the Calculator!")

try:
    # Prompt the user for operation type
    mode = input("Choose an operation type: arithmetic (A) or temperature conversion (T): ").strip().upper()

    if mode == "A":
        # Perform arithmetic operations
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a second number: "))
        operator = input("Enter an operator (+)/(-)/(*)/(/): ").strip()

        if operator == "+":
            result = num_1 + num_2
            print(f"The sum is: {result}")
        elif operator == "-":
            result = num_1 - num_2
            print(f"The difference is: {result}")
        elif operator == "*":
            result = num_1 * num_2
            print(f"The product is: {result}")
        elif operator == "/":
            if num_2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num_1 / num_2
                print(f"The quotient is: {result}")
        else:
            print("Invalid operator. Please use +, -, *, or /.")
    elif mode == "T":
        # Perform Celsius-to-Fahrenheit conversion
        temp_celsius = float(input("Enter the temperature in Celsius: "))
        temp_fahrenheit = round((temp_celsius * 9 / 5) + 32, 2)
        print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F.")
    else:
        print("Invalid mode selected. Please choose 'A' for arithmetic or 'T' for temperature conversion.")

except ValueError:
    print("Invalid input. Please enter numbers where required.")

print("Have a nice day!")
