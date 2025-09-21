import json  # built-in module for working with JSON

# 📖 What is JSON?
# JSON = JavaScript Object Notation.
# - A text-based format for storing and exchanging data.
# - Looks a lot like Python dictionaries/lists, but it’s language-independent → 
#   can be used in JavaScript, Python, Java, etc.
# - Commonly used in APIs, configuration files, and databases.
# - Differences from Python dict:
#     * JSON uses "true/false/null" instead of True/False/None.
#     * JSON keys/strings must be in double quotes (" ").
#     * JSON is always text; Python dict is an object in memory.

# Example Python dictionary inside a list (data to be converted)
data = [
   {
       "username": "Harsh-chauhan630",
       "email": "harsh@gmail.com",
       "password": "123456",   # storing as string is safer
       "student": True
   }
]

# ------------------------------
# Python → JSON string
# json.dumps() converts Python object into JSON formatted string
Uid = json.dumps(data, indent=4)  # indent=4 makes it human-readable
print(Uid)

# ------------------------------
# JSON string → Python
# json.loads() converts JSON string back into Python object
person = json.loads(Uid)
print(person)
