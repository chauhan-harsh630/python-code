# ================================
# 📌 Set in Python
# ================================

# A set is a built-in data type in Python that stores multiple UNIQUE values.
# ✅ Features:
# - Unordered → No fixed indexing
# - Mutable → You can add/remove elements
# - Unique → Duplicates are automatically removed
# - Heterogeneous → Can store different immutable types (int, str, tuple)

# --------------------------------
# Example 1: Creating a set
# --------------------------------
student = {"Harsh", "Akshay", "Ravi", "Samrath", "Sarthak", "Tushar", "Harsh", "Ravi"}
print("Initial set (duplicates removed):", student)

# --------------------------------
# Example 2: Adding & Removing
# --------------------------------
student.add("Abhay")        # Add new element
print("After adding Abhay:", student)

student.remove("Sarthak")   # Remove element (Error if not found)
print("After removing Sarthak:", student)

student.discard("Unknown")  # Safe remove (No error if not found)
print("After discarding Unknown (no error):", student)

# --------------------------------
# Example 3: Set Operations
# --------------------------------
A = {1, 2, 5, 4, 3}
B = {3, 5, 4, 2, 1, 6}

print("Union (A | B):", A | B)                   # Combine elements
print("Intersection (A & B):", A & B)            # Common elements
print("Difference (A - B):", A - B)              # Elements in A but not B
print("Symmetric Difference (A ^ B):", A ^ B)    # Elements in A or B but not both

# --------------------------------
# Example 4: Membership Test
# --------------------------------
print("Is 3 in A?", 3 in A)           # True
print("Is 7 in B?", 7 in B)           # False

# --------------------------------
# Example 5: Useful Set Functions
# --------------------------------
numbers = {10, 20, 30, 40, 50}
print("Length:", len(numbers))        # Count elements
print("Max:", max(numbers))           # Largest element
print("Min:", min(numbers))           # Smallest element
print("Sum:", sum(numbers))           # Sum of elements
print("Sorted Set:", sorted(numbers)) # Returns a sorted list
