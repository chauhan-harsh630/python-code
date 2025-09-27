# ============================
# What are decorators in Python?
# ============================
# - A decorator is a function that takes another function as input,
#   adds extra behavior, and returns a new function.
# - This allows us to "wrap" existing functions without changing their code.
# - The special @syntax is just a shortcut for applying decorators.

# ---------------------------------------------------------
# Example 1: Division decorator (makes division "smarter")
# ---------------------------------------------------------
def div(a, b):
    print(a / b)

def smart_div(func):
    def inner(a, b):
        # Ensure a is always larger than b before dividing
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

# Manual way: wrap div with smart_div
div1 = smart_div(div)
div1(2, 4)   # Output: 2.0 (instead of 0.5)


# ---------------------------------------------------------
# Example 2: Greeting decorator (adds a good morning message)
# ---------------------------------------------------------
def smart_greet(func):
    def inner(n):
        print("Good morning")   # Extra behavior
        return func(n)          # Call original function
    return inner

# Using @ syntax (cleaner than manual wrapping)
@smart_greet
def greet(n):
    print(f"Hello! my name is {n}")

greet("Harsh")
# Output:
# Good morning
# Hello! my name is Harsh


# ---------------------------------------------------------
# Example 3: Logging decorator (records function calls)
# ---------------------------------------------------------
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(5, 3)
# Output:
# Calling add with arguments (5, 3) {}
# add returned 8


# ---------------------------------------------------------
# Example 4: Timing decorator (measure function runtime)
# ---------------------------------------------------------
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished work!")

slow_function()
# Output:
# Finished work!
# slow_function took 2.000x seconds
