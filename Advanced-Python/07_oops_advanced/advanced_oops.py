# ===============================
# Class: Person
# ===============================
# Demonstrates a basic class with instance attributes, class attributes, and __repr__ method
class Person:
    # Class attribute: shared by all instances
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """
        Constructor to initialize a Person object
        :param name: str - Name of the person
        :param age: int - Age of the person
        """
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def __repr__(self):
        """
        Provides a string representation of the object.
        Useful for debugging and interactive display.
        """
        return f"Person({self.name!r}, {self.age})"


# ===============================
# Creating instances
# ===============================
p1 = Person("Harsh", 20)
p2 = Person("Riddhima", 19)
p3 = Person("Akshay", 19)
p4 = Person("Neha", 20)

# ===============================
# Accessing instance attributes
# ===============================
print(p1.name)  # Output: Harsh
print(p2.name)  # Output: Riddhima

# ===============================
# Additional Notes
# ===============================
# - Class attribute `species` is shared by all instances:
print(p1.species)  # Output: Homo sapiens
print(p2.species)  # Output: Homo sapiens

# - Instance attributes (`name`, `age`) are unique to each object
# - __repr__ helps when printing the object directly:
print(p1)  # Output: Person('Harsh', 20)
