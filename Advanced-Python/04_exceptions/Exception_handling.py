# Python Exception Handling Examples
# Exception handling allows us to handle runtime errors gracefully
# so the program doesn't crash unexpectedly.

# ---------------- Example 1: Handling ZeroDivisionError ----------------
try:
    # This will raise ZeroDivisionError if num is 0
    num = int(input("Enter a number for division: "))
    result = 10 / num
except ZeroDivisionError:
    # This block executes if a ZeroDivisionError occurs
    print("Error: You can't divide by zero!")
else:
    # Executes only if no exception occurs
    print("Result:", result)
finally:
    # Executes always, regardless of whether an exception occurred or not
    print("Execution completed for division example.\n")


# ---------------- Example 2: Raising and Handling ValueError ----------------
try:
    age = int(input("Enter your age: "))
    # Raise an exception if age is less than 18
    if age < 18:
        raise ValueError("You are too young to drive")
    print("You can drive 🚗")
except ValueError as e:
    # Catch the ValueError and print its message
    print("Error:", e)
finally:
    print("Execution completed for age check example.\n")


# ---------------- Example 3: Handling Multiple Exceptions ----------------
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    # This can raise ZeroDivisionError if num2 is 0
    result = num1 / num2
except ValueError:
    # Handles non-numeric input
    print("Error: Invalid input! Please enter valid numbers.")
except ZeroDivisionError:
    # Handles division by zero
    print("Error: You can't divide by zero!")
else:
    # Executes only if no exception occurs
    print("Result:", result)
finally:
    # Always executes
    print("Execution completed for multiple exception example.\n")
