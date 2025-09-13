# --------------------------------------------
# Python Basics - Variables and Data Types
# --------------------------------------------

# Numbers (int, float, complex)
x = 10           # int (whole number)
y = "Harsh"      # str (string)
z = 3.1456       # float (decimal)

print(x, y, z)

# Boolean (True / False)
loggeding = True   # bool
# None (represents "no value" like null in JS)
user = None        

print(loggeding, user)

# Type checking
x = "I am Harsh! Whatsup"
print(x, type(x))
print(type(x), type(y), type(z), type(loggeding), type(user))


# --------------------------------------------
# Strings
# --------------------------------------------
name = "Harsh Chauhan"
print(name[0:2])   # slicing (first two letters)
print(name[-1])    # last character

# String functions
print(name.upper())   # convert to UPPERCASE
print(name.lower())   # convert to lowercase
print(len(name))      # length of string


# --------------------------------------------
# Boolean logic
# --------------------------------------------
isAdmin = False
print(not loggeding)           # NOT operator
print(loggeding and isAdmin)   # AND operator
print(loggeding or isAdmin)    # OR operator


# --------------------------------------------
# Lists (like arrays in JS, but can store mixed types)
# --------------------------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])        # first element
fruits.append("mango")  # add item
print(fruits)


# --------------------------------------------
# Tuples (like lists but immutable)
# --------------------------------------------
colors = ("red", "green", "blue")
print(colors)
print(colors[1])   # access element
# colors[1] = "yellow"  # ❌ error (cannot modify tuple)


# --------------------------------------------
# Sets (unordered, unique values)
# --------------------------------------------
numbers = {1, 2, 3, 3, 4}
print(numbers)   # duplicates removed automatically


# --------------------------------------------
# Dictionaries (key-value pairs, like JS objects)
# --------------------------------------------
student = {
    "name": "Harsh",
    "age": 20,
    "isAdmin": False
}
print(student)
print(student["name"])      # access by key
print(student.get("age"))   # safer way to access


# --------------------------------------------
# Complex Numbers (less used, but supported in Python)
# --------------------------------------------
cnum = 2 + 3j
print(cnum, type(cnum))
print(cnum.real, cnum.imag)  # real and imaginary parts
