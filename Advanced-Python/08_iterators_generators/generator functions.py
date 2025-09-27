# ==========================================
# Iterators, Iteration Protocol, and Generators
# ==========================================

# ----------------------------
# Iteration protocol in Python
# ----------------------------

# 1. Iterable protocol
# An object is iterable if it has a __iter__() method that returns an iterator.
# Examples: lists, tuples, strings.

numbers = [1, 2, 3]
it = iter(numbers)   # get iterator from list

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # would raise StopIteration


# 2. Iterator protocol
# An object is an iterator if it implements both:
# - __iter__() → returns itself (the iterator)
# - __next__() → returns the next item, or raises StopIteration when finished

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

# Using the custom iterator
value = TopTen()
for i in value:
    print(i)  # prints 1 through 10


# ----------------------------
# What yield does
# ----------------------------
# - Gives a value back to whoever’s asking (like next() or a for loop).
# - Pauses the function’s execution right there, freezing all local variables.
# - When asked again (next()), it resumes from the exact point after yield, not from the start.

def demo():
    print("Start")
    yield 1
    print("Resumed")
    yield 2
    print("Done")
    yield None   # optional: signals end with an extra yield

g = demo()
print(next(g))  # "Start" then yields 1
print(next(g))  # "Resumed" then yields 2
print(next(g))  # "Done" then yields None
# next(g) would now raise StopIteration


# ----------------------------
# yield vs return
# ----------------------------
# return → ends the function completely, gives one value.
# yield  → gives a value but keeps the door open for more.

def with_return():
    return 5

def with_yield():
    yield 5
    yield 10

print(with_return())        # just 5
print(list(with_yield()))   # [5, 10]


# ----------------------------
# Generator functions
# ----------------------------
# A generator function is a normal function that uses yield instead of return.
# Each yield produces a value and pauses the function.
# Python automatically makes it an iterator.

def count(n):
    num = 1
    while num <= n:
        yield num
        num += 1

counter = count(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5
# print(next(counter))  # StopIteration if uncommented

# ----------------------------
# Comparison: normal function vs generator
# ----------------------------

# Normal function: creates the whole list in memory
def make_list(n):
    return [i for i in range(n)]

# Generator function: produces values one at a time, memory-efficient
def make_gen(n):
    for i in range(n):
        yield i

print(make_list(5))          # [0, 1, 2, 3, 4]
print(list(make_gen(5)))     # [0, 1, 2, 3, 4]
