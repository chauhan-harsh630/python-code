# ================================
# Object-Oriented Programming (OOP)
# ================================
# OOP is a way of programming that organizes code into "objects",
# which combine data (attributes) and behavior (methods/functions).

# -------------------------------
# 1. Class
# -------------------------------
# A class is like a blueprint or template for creating objects.
# Think of it as a cookie cutter: it defines the shape and features,
# but it isn’t the actual cookie yet.
# It defines attributes (data/state) and methods (behavior/functions).

class Person:
    # Class attribute
    species = "Homo sapiens"
   
    # Constructor (called automatically when object is created)
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# -------------------------------
# 2. Object
# -------------------------------
# An object is an instance of a class.
# Think of it as an actual cookie made from the cookie cutter.
# Each object has its own data but shares the structure defined by the class.

person1 = Person("Harsh", 20)
person2 = Person("Riddhima Sharma", 19)

# Accessing attributes and methods
print(person1.name)
person1.greet()
print("\n")
print(person2.name)
person2.greet()

# Accessing class attribute
print(person2.species)


# -------------------------------
# Analogy
# -------------------------------
# Class      → blueprint of a house
# Object     → actual house built from the blueprint
# Attributes → number of rooms, color, size
# Methods    → actions like open door, close window


# -------------------------------
# 3. What is __init__?
# -------------------------------
# __init__ is a special method in Python classes.
# It is called automatically when you create a new object of a class.
# Its main purpose is to initialize the object’s attributes (give the object its initial state).
# The first parameter of __init__ is always self, which represents the current object.
# You can add any number of parameters to __init__ to initialize your object.

class Instructor:
    def __init__(self):
        print("Creating a new Object")

# Creating objects of Instructor
instructor1 = Instructor()
instructor1.name = "Riddhi"
instructor1.address = "UP"
print(instructor1.name)

instructor2 = Instructor()
instructor2.name = "Akshay"
instructor2.address = "UP"
print(instructor2.name)
