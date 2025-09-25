# ================================================================================
# 📌 Python Data Structures - LIST
# ================================================================================

# ✅ What is a List in Python?
# A list is a collection data type in Python that can hold multiple values in a single variable.

# Key Features of a List:
# 1. Ordered      → Elements have a defined order (can be accessed by index).
# 2. Mutable      → You can change, add, or remove elements.
# 3. Allows duplicates → Same value can appear multiple times.
# 4. Heterogeneous → Can store different data types (int, string, float, etc.).
# ================================================================================

# ------------------------------------------------------------------------------
# 🐾 Example: Creating and Accessing List Elements
# ------------------------------------------------------------------------------
animals = ["Cat", "Dog", "Horse", "Elephant", "Monkey"]

print("First animal:", animals[0])    # Cat
print("Fourth animal:", animals[3])   # Elephant
print("Last animal:", animals[-1])    # Monkey

# ------------------------------------------------------------------------------
# 📝 Adding Elements
# ------------------------------------------------------------------------------
animals.insert(1, "Giraffe")    # Insert at index 1
print("After insert:", animals)

animals.append("Zebra")         # Add at the end
print("After append:", animals)

# ------------------------------------------------------------------------------
# 🗑️ Removing Elements
# ------------------------------------------------------------------------------
animals.remove("Giraffe")       # Remove by value
print("After remove:", animals)

popped = animals.pop()          # Remove last element
print("After pop:", animals, "| Popped:", popped)

# ------------------------------------------------------------------------------
# 🔢 Working with Numbers in Lists
# ------------------------------------------------------------------------------
numbers = [20, 30, 50, 40, 10]

print("Length:", len(numbers))      # 5
print("Sum:", sum(numbers))         # 150
print("Max:", max(numbers))         # 50
print("Min:", min(numbers))         # 10

# ------------------------------------------------------------------------------
# ✂️ Slicing Lists
# ------------------------------------------------------------------------------
print("Slice [0:4]:", numbers[0:4])   # [20, 30, 50, 40]
print("Last element:", numbers[-1])   # 10

# ------------------------------------------------------------------------------
# 🧮 List Comprehension
# ------------------------------------------------------------------------------
squares = [x**2 for x in numbers]
print("Squares:", squares)    # [400, 900, 2500, 1600, 100]

# ------------------------------------------------------------------------------
# 🔀 Sorting and Reversing
# ------------------------------------------------------------------------------
numbers.sort()
print("Sorted numbers:", numbers)   # [10, 20, 30, 40, 50]

numbers.reverse()
print("Reversed numbers:", numbers) # [50, 40, 30, 20, 10]

# ------------------------------------------------------------------------------
# 📚 Extra Useful List Methods
# ------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "banana"]

print("Count 'banana':", fruits.count("banana"))  # 2 occurrences
print("Index of 'cherry':", fruits.index("cherry"))

fruits_copy = fruits.copy()  # Make a shallow copy
print("Copy of fruits:", fruits_copy)

fruits.extend(["mango", "orange"])  # Add multiple items
print("After extend:", fruits)

fruits.clear()   # Remove all elements
print("After clear:", fruits)   # []
