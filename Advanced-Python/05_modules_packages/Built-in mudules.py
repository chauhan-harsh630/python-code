# --------------------- Built-in Modules in Python ---------------------

# --------------------- Math Module ---------------------
# Provides mathematical functions like sqrt, factorial, ceil, etc.
import math

print("Square root of 4:", math.sqrt(4))        # Square root of a number
print("Factorial of 5:", math.factorial(5))    # Factorial of a number
print("Ceiling of 5.2:", math.ceil(5.2))      # Rounds a number up to nearest integer
print("Value of pi:", math.pi)                 # Pi constant

print("\n")  # Just a separator for readability

# --------------------- Random Module ---------------------
# Used to generate random numbers or select random items
import random

print("Random integer between 1 and 10: ", random.randint(1, 10))
print("Random choice from list:", random.choice(["Apple", "Banana", "Peere"]))

print("\n")

# --------------------- OS Module ---------------------
# Provides functions to interact with the operating system
import os

print("Current working directory:", os.getcwd())   # Get current folder
print("Files/folders in current directory:", os.listdir())  # List files/folders
os.system("echo Hello World")                      # Execute a shell command
print("Default executable search path:", os.defpath)  # Default system path (string)

print("\n")

# --------------------- Datetime Module ---------------------
# Used to work with dates and times
import datetime

print("Current date and time:", datetime.datetime.now())  # Full date and time
print("Today's date:", datetime.date.today())             # Current date only

print("\n")

# --------------------- Additional Common Built-in Modules ---------------------
# 1. sys module - interact with Python runtime environment
import sys
print("Python version:", sys.version)  # Shows Python version

# 2. time module - time-related functions
import time
print("Current time (epoch):", time.time())  # Time in seconds since Jan 1, 1970

# 3. json module - work with JSON data
import json
data = {"name": "Riddhi", "age": 19}
json_string = json.dumps(data)  # Convert Python dict to JSON string
print("JSON string:", json_string)
