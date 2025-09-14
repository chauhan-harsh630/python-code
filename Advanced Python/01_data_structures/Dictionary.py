# 📌 What is a Dictionary in Python?
# A dictionary is a collection of key–value pairs.
# It is used to store data that is logically related (like a mapping).

# ✅ Key Features of Dictionary:
# - Key–Value Pair → Data is stored as {key: value}
# - Unique Keys → Keys must be unique, but values can be duplicated
# - Mutable → You can add, update, or remove items
# - Ordered (since Python 3.7) → Maintains insertion order
# - Keys must be immutable → e.g., string, number, tuple


# -----------------------------
# Creating a Dictionary
# -----------------------------
user = {
    "username": "Harsh-chauhan630",
    "email": "Test@gmail.com",
    "UId": "Harsh-Master"
}

# -----------------------------
# Accessing Values
# -----------------------------
print("Username:", user["username"])  # Access using key

# -----------------------------
# Updating Values
# -----------------------------
user["username"] = "Akshay-sharma930"  # Updating key value
print("Updated Username:", user["username"])

# -----------------------------
# Adding a New Key–Value Pair
# -----------------------------
user["role"] = "Student"
print("After Adding Role:", user)

# -----------------------------
# Removing Keys
# -----------------------------
# Using pop()
removed_value = user.pop("email")
print("Removed Email:", removed_value)
print("After pop():", user)

# Using del
del user["UId"]
print("After del:", user)

# -----------------------------
# Iterating through Dictionary
# -----------------------------
print("\nIterating through dictionary:")
for key, value in user.items():
    print(f"{key} → {value}")

# -----------------------------
# Dictionary Methods
# -----------------------------
print("\nDictionary Keys:", user.keys())
print("Dictionary Values:", user.values())
print("Dictionary Items:", user.items())
