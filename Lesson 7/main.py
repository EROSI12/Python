fruits = {
    "apple": 5,
    "banana": 1,
    "cherry": 9
}

try:
    # Try to access a key that does not exist in the dictionary
    print(fruits["pineapple"])

except KeyError:
    # Catch KeyError if the key doesn't exist in the dictionary
    print("This does not exist")

try:

    result = 10 / 2
    print(f"The result of (10) divided by (2) is: (result)")

except ZeroDivisionError:

    print("Error: Cannot divide by zero!")

