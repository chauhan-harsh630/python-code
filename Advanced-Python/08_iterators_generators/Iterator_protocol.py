# ==========================================
# Iteration Protocol in Python
# ==========================================

# ----------------------------
# 1. Iterable protocol
# ----------------------------
# An object is iterable if it has a __iter__() method that returns an iterator.
# Examples: lists, tuples, strings.

numbers = [1, 2, 3]
it = iter(numbers)   # get iterator from list

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # would raise StopIteration


# ----------------------------
# 2. Iterator protocol
# ----------------------------
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


# ----------------------------
# Using the custom iterator
# ----------------------------
value = TopTen()

for i in value:
    print(i)  # prints 1 through 10
