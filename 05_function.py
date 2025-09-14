# ================================
# 05_functions.py
# Functions in Python
# ================================
# Functions are reusable blocks of code designed to perform a task.
# Syntax:
#   def function_name(parameters):
#       """docstring (optional)"""
#       # code block
#       return value (optional)
# ================================


# --------------------------------
# 1. Simple Function
# --------------------------------
def greet():
    """Prints a simple greeting message."""
    print("Hello World!")


# --------------------------------
# 2. Calling a Function inside Another Function
# --------------------------------
def call():
    """Calls the greet() function inside itself."""
    greet()  # function call inside another function
    print("Now I am calling greet() function in call() function")


print("\n=== Example 1: Function Calling Another Function ===")
print("Call the call() function:")
call()


# --------------------------------
# 3. Function with Parameter
# --------------------------------
def goodwish(name):
    """Greets a user with a personalized good morning message."""
    print(f"Hello, good morning {name}!")


print("\n=== Example 2: Function with Parameter ===")
goodwish("Harsh")
goodwish("Rahul")


# --------------------------------
# 4. Function with Return Value
# --------------------------------
def sum(a, b):
    """Returns the sum of two numbers."""
    return a + b


print("\n=== Example 3: Function with Return Value ===")
print("Sum:", sum(5, 7))


# --------------------------------
# 5. Function with Default Argument
# --------------------------------
def power(base, exponent=2):
    """
    Returns base raised to the power of exponent.
    If exponent is not provided, defaults to 2 (square).
    """
    return base ** exponent


print("\n=== Example 4: Function with Default Argument ===")
print("Square of 4:", power(4))
print("4 to the power 3:", power(4, 3))


# --------------------------------
# 6. Function Returning Multiple Values
# --------------------------------
def calculator(a, b):
    """Returns multiple operations: sum, difference, product, and division."""
    return a + b, a - b, a * b, a / b


print("\n=== Example 5: Function Returning Multiple Values ===")
s, d, m, div = calculator(10, 5)
print("Sum:", s, "| Subtraction:", d, "| Multiplication:", m, "| Division:", div)


# --------------------------------
# 7. Lambda Function (Anonymous Function)
# --------------------------------
square = lambda x: x * x
add_nums = lambda a, b: a + b

print("\n=== Example 6: Lambda (Anonymous Functions) ===")
print("Square of 6:", square(6))
print("Sum of 4 and 5:", add_nums(4, 5))
