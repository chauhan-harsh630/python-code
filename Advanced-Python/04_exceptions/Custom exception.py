# --------------------- Custom Exception: Driving Age ---------------------
class AgeTooYoung(Exception):
    """Raised when the user is too young to drive"""
    pass

try:
    # Take user input for age
    age = int(input("Enter your age: "))
    
    # Check if user is under 18
    if age < 18:
        # Raise a custom exception if age is too low
        raise AgeTooYoung("You must be at least 18 to drive!")
except AgeTooYoung as e:
    # Catch the custom exception and display the message
    print("Custom error:", e)
else:
    # Runs if no exception occurs
    print("You can drive 🚗")
finally:
    # Always runs, used for cleanup or final messages
    print("Execution completed for driving age check.\n")


# --------------------- Custom Exception: Voting Age ---------------------
class AgeForVote(Exception):
    """Raised when the user is too young to vote"""
    def __init__(self, age, message="User is too young for vote"):
        self.age = age          # Store the age for reference
        self.message = message  # Default message
        # Pass a formatted message to the base Exception class
        super().__init__(f"{message}. Age provided: {age}")

try:
    # Take user input for voting age
    age = int(input("Enter your age for voting: "))
    
    # Check if user is under 18
    if age < 18:
        # Raise the custom exception with the user's age
        raise AgeForVote(age)
except AgeForVote as e:
    # Catch the custom exception and display detailed message
    print("Invalid Age!", e)
else:
    # Runs if no exception occurs
    print("Congratulations! You can vote now 🎉")
finally:
    # Always runs
    print("Age validation completed.\n")
