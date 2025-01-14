#miniräknare

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    # summan
    total = num1 + num2 + num3
    print("***********Python test************")
    print(f"You chose {num1}, {num2}, and {num3}")
    print(f"The sum of your numbers is: {total:.2f}")
    print("*********************************")

    # storsta
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    print(f"The highest number is: {largest}")
    print("*********************************")

    # 2 eller 3 lika
    if num1 == num2 == num3:
        print("All numbers are equal")
        print("*********************************")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("Two numbers are equal")
        print("*********************************")
    else:
        print("The numbers are all different")
        print("*********************************")

    # mellersta
    if num1 != num2 and num2 != num3 and num1 != num3:
        if (num1 < num2 < num3) or (num3 < num2 < num1):
            middle = num2
        elif (num2 < num1 < num3) or (num3 < num1 < num2):
            middle = num1
        else:
            middle = num3
        print(f"The middle number is: {middle}")
        print("*********************************")
    elif num1 == num2 == num3:
        print("The middle number is the same as all the numbers")
        print("*********************************")
    else:
        print("There is no middle number in this case.")
        print("*********************************")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
