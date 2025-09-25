# 🐍 02_strings/strings_all_in_one.py
# ---------------------------------------------------
# 📘 STRINGS IN PYTHON - COMPLETE NOTES + EXAMPLES
# ---------------------------------------------------
# A string is a sequence of characters enclosed in quotes.
# Strings are ordered, immutable, and iterable.
# ---------------------------------------------------

# ✅ Creating Strings
single = 'Hello'
double = "World"
multi = """This is
a multi-line
string."""

print("Single:", single)
print("Double:", double)
print("Multi-line:", multi)


# ---------------------------------------------------
# ✅ Indexing & Slicing
# ---------------------------------------------------
word = "Python"

print("\n🔹 Indexing & Slicing")
print("word[0]  →", word[0])    # First char
print("word[-1] →", word[-1])   # Last char
print("word[0:4] →", word[0:4]) # Slice from 0 to 3
print("word[:3]  →", word[:3])  # From start to index 2
print("word[2:]  →", word[2:])  # From index 2 to end


# ---------------------------------------------------
# ✅ String Operations
# ---------------------------------------------------
a, b = "Hello", "World"

print("\n🔹 String Operations")
print("Concatenation:", a + " " + b)
print("Repetition:", a * 3)
print("Membership:", 'H' in a, "|", 'z' not in b)
print("Length:", len(a))


# ---------------------------------------------------
# ✅ Escape Sequences
# ---------------------------------------------------
print("\n🔹 Escape Sequences")
print("Line1\nLine2")     
print("Tab\tSpace")       
print("She said: \"Python is fun!\"")  


# ---------------------------------------------------
# ✅ f-Strings (Formatting)
# ---------------------------------------------------
name, age = "Harsh", 20
print(f"\n🔹 My name is {name} and I am {age} years old.")


# ---------------------------------------------------
# ✅ Iterating over Strings
# ---------------------------------------------------
print("\n🔹 Looping through 'Code':")
for ch in "Code":
    print(ch)


# ---------------------------------------------------
# ✅ STRING METHODS
# ---------------------------------------------------
text = "  hello Python  "

print("\n🔹 String Methods")

# --- Case methods ---
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())

# --- Whitespace handling ---
print("Strip:", text.strip())
print("Lstrip:", text.lstrip())
print("Rstrip:", text.rstrip())

# --- Searching ---
print("Find 'Python':", text.find("Python"))   # index
print("Index of 'hello':", text.index("hello")) # like find(), but error if not found
print("Count of 'o':", text.count("o"))
print("Starts with '  h':", text.startswith("  h"))
print("Ends with 'n  ':", text.endswith("n  "))

# --- Replacing & Modifying ---
print("Replace:", text.replace("Python", "World"))
print("Center:", "Python".center(20, "-"))
print("Justify Left:", "Hi".ljust(10, "."))
print("Justify Right:", "Hi".rjust(10, "."))

# --- Checking methods ---
print("Is Alpha (letters only):", "Hello".isalpha())
print("Is Digit:", "12345".isdigit())
print("Is Alnum (letters+digits):", "Python3".isalnum())
print("Is Space:", "   ".isspace())
print("Is Title Case:", "Hello World".istitle())
print("Is Upper:", "HELLO".isupper())
print("Is Lower:", "hello".islower())

# --- Splitting & Joining ---
words = "Python is fun".split()   # default split by space
print("Split:", words)
print("Join:", "-".join(words))

csv = "a,b,c,d"
print("Split by comma:", csv.split(","))
print("Join with comma:", ",".join(["1","2","3"]))

# --- Zfill & Partition ---
print("Zfill (pad with zeros):", "42".zfill(5))  
print("Partition:", "Hello World".partition(" ")) # split into 3 parts

# --- Encoding ---
print("Encode UTF-8:", "Python".encode("utf-8"))

