# =====================================================
# 🐍 Python Datetime Module Tutorial
# =====================================================
# The datetime module in Python is a toolkit for working with dates and times.
# It provides classes and methods for:
#   - Getting the current date and time
#   - Creating specific dates and times
#   - Performing date arithmetic
#   - Formatting and parsing date/time strings
#   - Working with weekdays and timezones
# =====================================================

# Import necessary classes from datetime module
from datetime import datetime, timedelta, date, time
import calendar  # for mapping weekday numbers to names

# =====================================================
# 1️⃣ Getting Current Date and Time
# =====================================================
now = datetime.now()  # current local date and time

# Get day name using strftime
day_name = now.strftime("%A")  # Full weekday name, e.g., 'Saturday'

print("Current Date and Time :", now)
print("Current Date          :", now.date())
print("Current Time          :", now.time())
print("Today is             :", day_name)

# =====================================================
# 2️⃣ Creating Specific Dates and Times
# =====================================================
# You can create your own date, time, or combined datetime objects
d = date(2025, 10, 18)           # Year, Month, Day
t = time(14, 30, 0)              # Hour, Minute, Second
dt = datetime(2025, 10, 18, 14, 30, 0)  # Year, Month, Day, Hour, Minute, Second

print("\nSpecific Date :", d)
print("Specific Time :", t)
print("Specific Date & Time :", dt)

# =====================================================
# 3️⃣ Date Arithmetic using timedelta
# =====================================================
# timedelta allows you to add or subtract time (days, seconds, etc.)
present = datetime.now()          # reference point
next_week = present + timedelta(days=7)   # 7 days ahead
yesterday = present - timedelta(days=2)   # 2 days ago

# Get day names for each date
present_day = present.strftime("%A")
yesterday_day = yesterday.strftime("%A")
next_week_day = next_week.strftime("%A")

print("\nDate Arithmetic Examples:")
print(f"Present      : {present}  | Day: {present_day}")
print(f"Yesterday    : {yesterday}  | Day: {yesterday_day}")
print(f"Next Week    : {next_week}  | Day: {next_week_day}")

# =====================================================
# 4️⃣ Using calendar module to get weekday name
# =====================================================
# weekday() returns integer 0 (Monday) to 6 (Sunday)
# calendar.day_name maps integers to full weekday names
weekday_name = calendar.day_name[present.weekday()]
print("\nWeekday using calendar module:", weekday_name)

# =====================================================
# 5️⃣ Extra Tips / Notes
# =====================================================
# - Use '%a' in strftime for short weekday names, e.g., 'Sat'
# - timedelta can also handle weeks, hours, minutes, seconds
# - For parsing date strings, use datetime.strptime()
# - For formatting datetime as strings, use datetime.strftime()
# - This module is foundational for logging, scheduling, countdowns, and AI projects involving time-series
