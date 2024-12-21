def simple_calculator():
    print("Welcome to the Simple Calculator!")

    try:

        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")


        num1 = float(num1)
        num2 = float(num2)


        operation = input("Enter operation (+, -, *, /): ")


        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':

            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation! Please choose +, -, *, or /.")

        print(f"The result of (num1) (operation) (num2) = (result)")

    except ValueError as e:
        print(f"Error: (e)")
    except ZeroDivisionError as e:
        print(f"Error: (e)")
    except Exception as e:
        print(f"An unexpected error occurred: (e)")
    finally:
        print("Thank you for using the Simple Calculator!")


simple_calculator()

fruits = {
    "apple": 5,
    "banana": 1,
    "cherry": 9
}

try:

    print(fruits["pineapple"])
except KeyError:

    print("This does not exist")

try:

    result = 10 / 2
    print(f"The result of (10) divided by (2) is: (result)")

except ZeroDivisionError:

    print("Error: Cannot divide by zero!")


