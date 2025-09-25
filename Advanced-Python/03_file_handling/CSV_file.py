# ---------------------------------------
# 📌 Working with CSV in Python
# ---------------------------------------
# CSV (Comma Separated Values) is used to store tabular data
# like spreadsheets or simple databases.

import csv

# -----------------------------
# Writing data into a CSV file
# -----------------------------
with open("student.txt", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "id"])  # Header row
    writer.writerow(["Harsh", 20, "harsh-chaun630"])
    writer.writerow(["Riddhi", 19, "riddhi-pvt"])
    writer.writerow(["Akshay", 20, "akshay-sharma001"])
    writer.writerow(["Ritik", 19, "rithik-baha007"])

# -----------------------------
# Reading data from CSV file
# -----------------------------
with open("student.txt", "r") as file:
    reader = csv.DictReader(file)  # Treats first row as column headers
    for row in reader:
        if row["id"] == "riddhi-pvt":
            print("\nFrom CSV →", row["Name"], row["Age"], row["id"])


with open("student.txt","r") as file:
    reader = csv.reader(file)
    print("\n All Students ")
    for row in reader:
        print(row)            


# ---------------------------------------
# 📌 Working with Dictionaries in Python
# ---------------------------------------
# A dictionary is like a mini database in memory,
# storing data as key–value pairs.

users = [
    {
        "username": "Riddhi",
        "id": "itz-pvt-queen",
        "email": "riddhi-sharma@gmail.com",
    },
    {
        "username": "Harsh",
        "id": "defend.404",
        "email": "harshchauhan@gmail.com",
    },
]

# -----------------------------
# Searching in list of dictionaries
# -----------------------------
for u in users:
    if u["username"] == "Riddhi":
        print("\nFrom Dictionary →", u["username"], u["id"], u["email"])
