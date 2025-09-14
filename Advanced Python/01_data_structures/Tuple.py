# ================================================================================
# 📌 Python Data Structures - TUPLE
# ================================================================================

# ✅ What is a Tuple?
# A tuple is a collection data type in Python that is:
# - Ordered (elements have fixed positions, accessed via index)
# - Immutable (cannot be modified after creation)
# - Allows duplicates
# - Can hold heterogeneous data types

# ================================================================================

# ------------------------------------------------------------------------------
# 🐾 Creating a Tuple and Accessing Elements
# ------------------------------------------------------------------------------
person = ("Harsh", 20, "BCA")

# Tuple unpacking (assigning tuple values to variables)
name, age, course = person
print("Name: ", name)
print("Age: ", age)
print("Course: ", course)

# Accessing elements with index
number = ("Apple", 123)
print("First element:", number[0])   # Apple
print("Second element:", number[1])  # 123

# ------------------------------------------------------------------------------
# 🧮 Tuple with Numbers (Basic Operations)
# ------------------------------------------------------------------------------
num = (10, 30, 50, 20, 40)

print("Tuple:", num)
print("Length:", len(num))         # Total number of elements
print("Sum:", sum(num))            # Sum of all elements
print("Max:", max(num))            # Largest element
print("Min:", min(num))            # Smallest element

# ------------------------------------------------------------------------------
# ✂️ Tuple Slicing
# ------------------------------------------------------------------------------
print("Slice [1:4]:", num[1:4])    # (30, 50, 20)
print("Last element:", num[-1])    # 40

# ------------------------------------------------------------------------------
# 🔄 Tuple Methods
# ------------------------------------------------------------------------------
numbers_tuple = (10, 20, 30, 10, 40)

print("Count of 10:", numbers_tuple.count(10))  # 2
print("Index of 30:", numbers_tuple.index(30))  # 2

# ------------------------------------------------------------------------------
# 📚 Nested Tuple
# ------------------------------------------------------------------------------
nested_tuple = (("Math", 90), ("English", 85), ("Science", 95))
print("Nested Tuple:", nested_tuple)
print("Access English Marks:", nested_tuple[1][1])  # 85

# ------------------------------------------------------------------------------
# 🔗 Tuple vs List
# ------------------------------------------------------------------------------
# List → Mutable (can be changed)
# Tuple → Immutable (fixed once created)
