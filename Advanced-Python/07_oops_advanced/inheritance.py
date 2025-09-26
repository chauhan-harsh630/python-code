# ==========================================
# Property and Descriptors — Controlling Attribute Access
# ==========================================
# - @property is a built-in Python descriptor for single attributes.
# - Custom descriptors allow reusable rules like type checking, validation, lazy loading.
# - Useful when multiple attributes share similar rules or logic.

# --------------------------
# Descriptor Class: Typed
# --------------------------
class Typed:
    def __init__(self, typ):
        """
        :param typ: expected type for the attribute (e.g., int, str)
        """
        self.typ = typ
        self.name = None  # Will be set when the descriptor is assigned to a class attribute

    def __set_name__(self, owner, name):
        """
        Called when the descriptor is assigned to a class attribute.
        Saves the attribute name for later reference.
        """
        self.name = name

    def __get__(self, instance, owner):
        """
        Called when accessing the attribute.
        Returns the descriptor itself if accessed via the class.
        """
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        """
        Called when assigning a value to the attribute.
        Enforces type checking.
        """
        if not isinstance(value, self.typ):
            raise TypeError(f"{self.name!r} must be {self.typ.__name__}")
        instance.__dict__[self.name] = value

# --------------------------
# Using the Descriptor
# --------------------------
class Person:
    # Applying Typed descriptor to enforce types on multiple attributes
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        # Descriptor automatically checks types
        self.name = name
        self.age = age

# --------------------------
# Testing / Usage
# --------------------------
p1 = Person("Riddhi", 19)
print(p1.name)  # Riddhi
print(p1.age)   # 19

# Uncommenting the following line would raise a TypeError
# p1.age = "twenty"  # TypeError: 'age' must be int

# --------------------------
# Key Concepts
# --------------------------
# 1. Descriptor Protocol:
#    - __get__: invoked on attribute access
#    - __set__: invoked on attribute assignment
#    - __set_name__: called when the descriptor is first assigned in the class
# 2. Descriptors enforce consistent rules for multiple attributes.
# 3. @property is suitable for single attributes; custom descriptors excel when multiple attributes share logic.
