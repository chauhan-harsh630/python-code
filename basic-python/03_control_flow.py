# ================================
# 03_control_flow.py
# Control Flow in Python
# ================================
# Control flow decides how the program runs:
# - Make decisions (if, elif, else)
# - Repeat tasks (loops)
# - Control loop execution (break, continue, pass)
# ================================


# ==================================================
# Example 1: Driving Age Check
# ==================================================
print("\n=== Example 1: Driving Eligibility ===")
age = int(input("Enter your age: "))

# if-else statement for decision making
if age >= 18:
    print("✅ You can drive")
else:
    print("❌ You can't drive")


# ==================================================
# Example 2: Grading System
# ==================================================
print("\n=== Example 2: Grading System ===")
marks = int(input("Enter your marks: "))

# Using if-elif-else for multiple conditions
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# ==================================================
# Example 3: Even or Odd Number
# ==================================================
print("\n=== Example 3: Even or Odd ===")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# ==================================================
# Example 4: Simple Login System
# ==================================================
print("\n=== Example 4: Simple Login ===")
username = input("Enter username: ")
password = input("Enter password: ")

# Nested if: condition inside condition
if username == "admin":
    if password == "1234":
        print("✅ Login Successful")
    else:
        print("❌ Wrong Password")
else:
    print("❌ Username not found")
