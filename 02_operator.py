# ================================
# 02_operator.py
# Demonstration of Python Operators
# ================================
# In Python, operators are symbols used to perform operations 
# on values and variables. 
# Example: +, -, *, /, ==, and, in, is etc.
# ================================


# ==================================================
# 1. Arithmetic Operators
# ==================================================
# Used for basic mathematical calculations
# + (Addition), - (Subtraction), * (Multiplication), 
# / (Division), // (Floor Division), % (Modulus), ** (Exponent)
a = 9
b = 7

print("\n=== 1. Arithmetic Operators ===")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b):", a % b)
print("Exponentiation (a ** b):", a ** b)


# ==================================================
# 2. Comparison (Relational) Operators
# ==================================================
# Used to compare two values
# ==, !=, >, <, >=, <=
x = 5
y = 10

print("\n=== 2. Comparison Operators ===")
print("Equal (x == y):", x == y)
print("Not Equal (x != y):", x != y)
print("Greater Than (x > y):", x > y)
print("Less Than (x < y):", x < y)
print("Greater or Equal (x >= y):", x >= y)
print("Less or Equal (x <= y):", x <= y)


# ==================================================
# 3. Logical Operators
# ==================================================
# Used to combine conditions
# and, or, not
p = True
q = False

print("\n=== 3. Logical Operators ===")
print("AND (p and q):", p and q)   # True only if both are True
print("OR (p or q):", p or q)      # True if at least one is True
print("NOT (not p):", not p)       # Negates the value


# ==================================================
# 4. Assignment Operators
# ==================================================
# Used to assign values with shorthand operations
# =, +=, -=, *=, /=, %=, **=, //=
a = 5
print("\n=== 4. Assignment Operators ===")
print("Initial value of a:", a)

a += 2   # a = a + 2
print("After a += 2:", a)

a -= 3   # a = a - 3
print("After a -= 3:", a)

a *= 2   # a = a * 2
print("After a *= 2:", a)

a /= 4   # a = a / 4
print("After a /= 4:", a)

a %= 2   # a = a % 2
print("After a %= 2:", a)

a **= 3  # a = a ** 3
print("After a **= 3:", a)


# ==================================================
# 5. Bitwise Operators
# ==================================================
# Work on binary representation of numbers
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)
x = 6   # Binary: 110
y = 3   # Binary: 011

print("\n=== 5. Bitwise Operators ===")
print("AND (x & y):", x & y)     
print("OR (x | y):", x | y)     
print("XOR (x ^ y):", x ^ y)     
print("NOT (~x):", ~x)          
print("Left Shift (x << 2):", x << 2)  
print("Right Shift (x >> 1):", x >> 1) 


# ==================================================
# 6. Membership Operators
# ==================================================
# Check if a value exists in a sequence (list, string, tuple, etc.)
# in, not in
nums = [1, 2, 3, 4]

print("\n=== 6. Membership Operators ===")
print("2 in nums:", 2 in nums)      
print("5 not in nums:", 5 not in nums)  


# ==================================================
# 7. Identity Operators
# ==================================================
# Compare memory locations of two objects
# is, is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\n=== 7. Identity Operators ===")
print("a is b:", a is b)         # True (same memory reference)
print("a is c:", a is c)         # False (different objects, same values)
print("a is not c:", a is not c) # True
