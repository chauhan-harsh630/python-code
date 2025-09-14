# ================================
# 04_loops.py
# Loops in Python
# ================================
# Loops allow repeating a block of code multiple times.
#
# Working Principle:
#   Start -> Check condition -> Execute block -> Update counter -> Repeat
#   -> Exit when condition becomes False.
#
# Types of Loops in Python:
#   1. for loop  (fixed number of iterations)
#   2. while loop (runs until condition fails)
#   3. nested loops (loop inside another loop)
#   4. loop control statements: break, continue, pass
# ================================


# --------------------------------
# 1. for loop (fixed iterations)
# --------------------------------
print("\n=== Example 1: for loop with range() ===")
for i in range(1, 6):  # range(start, stop) -> stop is excluded
    print(i)


# --------------------------------
# 2. Sum of numbers using for loop
# --------------------------------
print("\n=== Example 2: Sum of first 10 numbers ===")
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)


# --------------------------------
# 3. Iterating over a string
# --------------------------------
print("\n=== Example 3: Characters in a string ===")
for char in "Python":
    print(char)


# --------------------------------
# 4. while loop (unknown iterations)
# --------------------------------
print("\n=== Example 4: Countdown using while ===")
count = 5
while count > 0:
    print(count)
    count -=1
print("Blast Off! 🚀")


# --------------------------------
# 5. while loop with user input
# --------------------------------
print("\n=== Example 5: Simple Menu with while ===")
while True:
    choice = input("Type 'exit' to quit: ")
    if choice.lower() == "exit":
        print("Goodbye!")
        break
    else:
        print("You typed:", choice)


# --------------------------------
# 6. Nested Loops (loop inside another loop)
# --------------------------------
print("\n=== Example 6: Nested Loop (Pattern Printing) ===")
for i in range(1, 6):  # Outer loop -> rows
    for j in range(1, i + 1):  # Inner loop -> columns
        print("*", end=" ")
    print()  # move to next line


# --------------------------------
# 7. Loop Control Statements
# --------------------------------
print("\n=== Example 7: Loop Control Statements ===")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3 (continue)")
        continue
    if i == 5:
        print("Breaking at 5")
        break
    print("Number:", i)


# --------------------------------
# 8. pass statement
# --------------------------------
print("\n=== Example 8: pass statement ===")
for i in range(1, 4):
    pass  # does nothing (placeholder for future code)
print("Loop ran but did nothing with 'pass'")
