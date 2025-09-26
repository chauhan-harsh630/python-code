# ==========================================
# Property and Descriptors — Controlling Attribute Access
# ==========================================
# - @property is a simple built-in descriptor in Python.
# - Custom descriptors allow reusable rules like type checking, validation, lazy loading, etc.
# - Descriptors are useful when you want the same rule applied to multiple attributes or classes.

# --------------------------
# Descriptor Class: Typed
# --------------------------
class Typed:
    def __init__(self, typ):
        """
        :param typ: expected type for the attribute (e.g., int, str)
        """
        self.typ = typ       # Type to enforce
        self.name = None     # Attribute name, set later by __set_name__

    def __set_name__(self, owner, name):
        """
        Called when the descriptor is assigned to a class attribute.
        Stores the attribute name for reference.
        """
        self.name = name

    def __get__(self, instance, owner):
        """
        Called when the attribute is accessed.
        If accessed via class, returns the descriptor itself.
        """
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        """
        Called when the attribute is set.
        Enforces type checking.
        """
        if not isinstance(value, self.typ):
            raise TypeError(f"{self.name!r} must be {self.typ.__name__}")
        instance.__dict__[self.name] = value

# --------------------------
# Using the Descriptor
# --------------------------
class Person:
    # Using Typed descriptor for type enforcement on multiple attributes
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        # Descriptor automatically enforces type
        self.name = name
        self.age = age

# --------------------------
# Testing / Usage
# --------------------------
p1 = Person("Riddhi", 19)
print(p1.name)  # Output: Riddhi
print(p1.age)   # Output: 19

# Attempting wrong type raises an error
# p1.age = "twenty"  # TypeError: 'age' must be int

# --------------------------
# Additional Notes
# --------------------------
# 1. Descriptor Protocol:
#    - __get__ : called when accessing the attribute
#    - __set__ : called when assigning a value
#    - __set_name__ : called when the descriptor is first assigned in class
# 2. Descriptors allow reusable rules across multiple attributes.
# 3. Compared to @property:
#    - @property is simpler for a single attribute.
#    - Custom descriptors are better when multiple attributes share similar logic.
