# ====================================
# Python Comprehensions Examples
# ====================================

# -------------------------
# 1. List Comprehension
# -------------------------
# Create a list of squares for numbers 0 to 4
s = [x**2 for x in range(5)]
print("Squares:", s)  # Output: [0, 1, 4, 9, 16]


# -------------------------
# 2. List Comprehension with Condition
# -------------------------
# Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)  # Output: [0, 2, 4, 6, 8]


# -------------------------
# 3. Dictionary Comprehension
# -------------------------
# Create a dictionary mapping each number to its square
new_square = {x: x**2 for x in range(5)}
print("Number-Square mapping:", new_square)  
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
