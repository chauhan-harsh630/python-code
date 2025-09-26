# ==========================================
# Property and Descriptors — Controlling Attribute Access
# ==========================================
# - @property is a simple built-in descriptor in Python
# - Custom descriptors allow reusable rules like type checking, validation, lazy loading, etc.

# --------------------------
# Descriptor Class: Typed
# --------------------------
class Typed:
    def __init__(self, typ):
        """
        :param typ: expected type for the attribute (e.g., int, str)
        """
        self.typ = typ       # Type to enforce
        self.name = None     # Attribute name, set later

    def __set_name__(self, owner, name):
        """
        Called when the descriptor is assigned to a class attribute.
        Stores the attribute name for reference.
        """
        self.name = name

    def __get__(self, instance, owner):
        """
        Called when the attribute is accessed.
        """
        if instance is None:
            return self   # Accessed via class, return descriptor itself
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
    # Using Typed descriptor for type enforcement
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name  # Type checked by Typed descriptor
        self.age = age    # Type checked by Typed descriptor

# --------------------------
# Testing
# --------------------------
p1 = Person("Riddhi", 19)
print(p1.name)  # Output: Riddhi
print(p1.age)   # Output: 19

# --------------------------
# Notes / Concepts
# --------------------------
# 1. Descriptor Protocol: __get__, __set__, __set_name__ methods
# 2. Enforces rules for attributes across multiple instances without duplicating code
# 3. Custom descriptors are more reusable than simple @property decorators
# 4. Attempting wrong type will raise a TypeError:
#    p1.age = "twenty"  # TypeError: 'age' must be int
